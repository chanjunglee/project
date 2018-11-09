# coding: utf-8

# In[ ]:

import numpy as np
import librosa # 파이썬 음악파일 분석 라이브러리
import math
import re
import os

class ClassicFeatureData:
    hop_length = None # 
    composer_list = ['bach','beethoven','chopin','debussy','mozart']

    dir_trainfolder = "./classic_data/train"
    dir_devfolder = "./classic_data/validation"
    dir_testfolder = "./classic_data/test"

    #     dir_all_files = "./classic_data/" # 없어도 될듯

    train_X_preprocessed_data = 'data_train_input.npy'
    train_Y_preprocessed_data = 'data_train_target.npy'
    dev_X_preprocessed_data = 'data_validation_input.npy'
    dev_Y_preprocessed_data = 'data_validation_target.npy'
    test_X_preprocessed_data = 'data_test_input.npy'
    test_Y_preprocessed_data = 'data_test_target.npy'

    train_X = train_Y = None
    dev_X = dev_Y = None
    test_X = test_Y = None

    def __init__(self):
        self.hop_length = 512
        self.timeseries_length_list = [] 

    def load_preprocess_data(self): # 시작 코드
        self.trainfiles_list = self.path_to_wavfiles(self.dir_trainfolder) # 경로 + 모든 파일을 리턴받는다.
        self.devfiles_list = self.path_to_wavfiles(self.dir_devfolder)
        self.testfiles_list = self.path_to_wavfiles(self.dir_testfolder)
        
        all_files_list = []
        all_files_list.extend(self.trainfiles_list) # wav 각 폴더의 모든 파일 이름 리스트에 추가
        all_files_list.extend(self.devfiles_list)
        all_files_list.extend(self.testfiles_list)

        #self.precompute_min_timeseries_len(all_files_list)
        print("[DEBUG] total number of files: " + str(len(self.timeseries_length_list))) # extract_audio_features 

        # Training set
        self.train_X, self.train_Y = self.extract_wav_features(self.trainfiles_list)
        with open(self.train_X_preprocessed_data, 'wb') as f:
            np.save(f, self.train_X)
        with open(self.train_Y_preprocessed_data, 'wb') as f:
            self.train_Y = self.one_hot(self.train_Y)
            np.save(f, self.train_Y)
#         print("1.train_X", self.train_X ,"1.train_Y", self.train_Y)

        # Validation set
        self.dev_X, self.dev_Y = self.extract_wav_features(self.devfiles_list)
        with open(self.dev_X_preprocessed_data, 'wb') as f:
            np.save(f, self.dev_X)
        with open(self.dev_Y_preprocessed_data, 'wb') as f:
            self.dev_Y = self.one_hot(self.dev_Y)
            np.save(f, self.dev_Y)
#         print("1.Validation_X", self.dev_X ,"1.Validation_Y", self.dev_Y)
        
        # Test set
        self.test_X, self.test_Y = self.extract_wav_features(self.testfiles_list)
        with open(self.test_X_preprocessed_data, 'wb') as f:
            np.save(f, self.test_X)
        with open(self.test_Y_preprocessed_data, 'wb') as f:
            self.test_Y = self.one_hot(self.test_Y)
            np.save(f, self.test_Y)
#         print("1.test_X", self.test_X ,"1.test_Y", self.test_Y)

    def load_deserialize_data(self):
        self.train_X = np.load(self.train_X_preprocessed_data)
        self.train_Y = np.load(self.train_Y_preprocessed_data)
#         print("2.train_X", self.train_X ,"2.train_Y", self.train_Y)

        self.dev_X = np.load(self.dev_X_preprocessed_data)
        self.dev_Y = np.load(self.dev_Y_preprocessed_data)
#         print("2.Validation_X", self.dev_X ,"2.Validation_Y", self.dev_Y)
        
        self.test_X = np.load(self.test_X_preprocessed_data)
        self.test_Y = np.load(self.test_Y_preprocessed_data)
#         print("2.test_X", self.test_X ,"2.test_Y", self.test_Y)

    def precompute_min_timeseries_len(self, list_of_wavfiles):
        for file in list_of_wavfiles:
            print("Loading " + str(file))
            y, sr = librosa.load(file) # 수정
            self.timeseries_length_list.append(math.ceil(len(y) / self.hop_length))

    def extract_wav_features(self, list_of_wavfiles):
        #timeseries_length = min(self.timeseries_length_list)
        timeseries_length = 128
        data = np.zeros((len(list_of_wavfiles), timeseries_length, 33), dtype=np.float64) # 33 -> 40
        target = []

        for i, file in enumerate(list_of_wavfiles):
            y, sr = librosa.load(file)
            mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=self.hop_length, n_mfcc=13) # 
            spectral_center = librosa.feature.spectral_centroid(y=y, sr=sr, hop_length=self.hop_length) # 
            chroma = librosa.feature.chroma_stft(y=y, sr=sr, hop_length=self.hop_length) #
            spectral_contrast = librosa.feature.spectral_contrast(y=y, sr=sr, hop_length=self.hop_length) #
#             tempogram = librosa.feature.tempogram(y=y, sr=sr, hop_length=self.hop_length) # 
            
            splits = re.split('[_]', file)
            composer = re.split('[/]', splits[1])[2]
            target.append(composer)

            data[i, :, 0:13] = mfcc.T[0:timeseries_length, :] # 일반적인 분석 주파수 Hz : 1초에 진동하는 수
            data[i, :, 13:14] = spectral_center.T[0:timeseries_length, :] # 스펙트럼 중심
            data[i, :, 14:26] = chroma.T[0:timeseries_length, :] # 음높이 스케일관련 명도,채도와 옥타브 표현 14:26
            data[i, :, 26:33] = spectral_contrast.T[0:timeseries_length, :] # 스펙트럼 대비 계산 26:33
#             data[i, :, 30:33] = tempogram.T[0:timeseries_length, :] # 템포 

            print("Extracted features wav track %i of %i." % (i + 1, len(list_of_wavfiles)))
#             print("data",data, "label", np.expand_dims(np.asarray(target), axis=1))

        return data, np.expand_dims(np.asarray(target), axis=1)
# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.expand_dims.html

    def one_hot(self, Y_composer_strings):
        y_one_hot = np.zeros((Y_composer_strings.shape[0], len(self.composer_list)))
        for i, composer_string in enumerate(Y_composer_strings):
            index = self.composer_list.index(composer_string)
            y_one_hot[i, index] = 1
        return y_one_hot

    def path_to_wavfiles(self, dir_folder):
        list_of_wav = []
        for file in os.listdir(dir_folder):
            if file.endswith(".wav"):
                directory = "%s/%s" % (dir_folder, file)
                list_of_wav.append(directory)
        return list_of_wav

