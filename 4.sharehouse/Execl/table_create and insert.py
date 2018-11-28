# -*- coding: utf-8 -*-

'''

db에 연결하여 각 엑셀 csv파일에 해당되는 테이블을 생성, 자료를 입력합니다.

'''

from Model import *
from Db_Server import db_server

db_server.db_connect()
print('DB연결에 성공했습니다.')

Inter_Code.table_create()
print('Inter_Code 테이블 생성 완료')
Inter_Code.insert_interest()
print('Inter_Code 자료 입력 완료')

#
# Living_Pop.table_create()
# print('Living_Pop 테이블 생성 완료')
# Living_Pop.insert_interest()
# print('Living_Pop 자료 입력 완료')

# Old_Building.table_create()
# print('Old_Building 테이블 생성 완료')
# Old_Building.insert_interest()
# print('Old_Building 자료 입력 완료')
#
# Buy_Sell.table_create()
# print('Buy_Sell 테이블 생성 완료')
# Buy_Sell.insert_interest()
# print('Buy_Sell 자료 입력 완료')
#
# Bjd_Code.table_create()
# print('Bju_Code 테이블 생성 완료')
# Bjd_Code.insert_interest()
# print('Bju_Code 자료 입력 완료')
#
# Univ.table_create()
# print('Univ 테이블 생성 완료')
# Univ.insert_interest()
# print('Univ 자료 입력 완료')
#
# Comm_Reg.table_create()
# print('Comm_Reg 테이블 생성 완료')
# Comm_Reg.insert_interest()
# print('Comm_Reg 자료 입력 완료')
#
# Gathering_Fac.table_create()
# print('Gathering_Fac 테이블 생성 완료')
# Gathering_Fac.insert_interest()
# print('Gathering_Fac 자료 입력 완료')

# Bus.table_create()
# print('Bus 테이블 생성 완료')
# Bus.insert_interest()
# print('Bus 자료 입력 완료')

# Bus_line.table_create()
# print('Bus_line 테이블 생성 완료')
# Bus_line.insert_interest()
# print('Bus_line 자료 입력 완료')
#
# House_rent.table_create()
# print('House_rent 테이블 생성 완료')
# House_rent.insert_interest()
# print('House_rent 자료 입력 완료')
#
# Metro.table_create()
# print('Metro 테이블 생성 완료')
# Metro.insert_interest()
# print('Metro 자료 입력 완료')

print('Success')