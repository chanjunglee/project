# 성경 빈도수에 따른 등장인물 관계 분석
setwd("C:/Users/Administrator/Desktop/R")

library(rvest)

library(stringr)

library(igraph)

library(corrplot)

###  마태오 복음 크롤링(정제까지)

matthew1<-NULL

matthew<-NULL

for(i in 1:28){
  url_scripts <- paste0('http://maria.catholic.or.kr/bible/read/bible_read.asp?m=1&n=147&p=',i)
  
  html_scripts = read_html(url_scripts, encoding = "UTF-8")
  
  matthew <- html_scripts %>% html_nodes("#font_chg") %>% html_text() # table id가 font_chg인 텍스트 가져오기 
  
  # matthew <- str_trim(gsub('\\(.*\\)',' ',matthew) ) # 필요없는 괄호 부분(내용부분포함) 처리
  
  matthew <- str_trim(gsub('\\(.*?\\)','',matthew))
  
  matthew <- str_trim(gsub('\r|\t|\n|\\▶|\\▼|\\.|\\,|\\;|\\:|[A-z0-9]',' ',matthew) ) # 특수문자제거,영어,숫자제거
  
  matthew <- str_trim(gsub('\'|\\|\"|\\?|\\!|\\\"','',matthew) ) 
  
  matthew <- strsplit(matthew,split="       ")  #  양 끝에 있는 '   '처리 
  
  matthew <- as.data.frame(matthew) 
  
  matthew <- matthew[matthew != ""] 
  
  #matthew <- grep('[^A-z0-9]',matthew)
  
  #genesis<-data.frame(genesis) 
  
  matthew1 <- append(matthew1, values=c(matthew,'\n'))
  
}



## trim 함수 생성

trim <- function (x) gsub("^\\s+|\\s+$", "", x)

#guess_encoding('http://maria.catholic.or.kr/bible/read/bible_read.asp?m=1&n=147&p=1')

# 인물 목록 list (.txt)
crt<-read.csv("characters.txt", stringsAsFactors = T)

#crt

str(crt)

length(crt)

crt<-table(crt)

crt_k <- names( crt[crt>0]  )

#length(matthew1)

#matthew1[574]

#grep(crt_k[1], matthew1)

#which(crt_k[1],matthew1)


### 간단한 위치 확인


for (i in 1:length(crt_k)){
  
  cnt<-length(grep(crt_k[i], matthew1)) 
  
  where<-grep(crt_k[i], matthew1) 
  
  where1<-append(where,NULL) 
  
  print(paste(crt_k[i],cnt)) 
  
  print(where1) 
  
}

#####

# 특정 인물의 빈도 수와 예수와의 출현정도 비교

matching_charaters_fun <- function(){
  
  graphics.off()
  
  cn <-menu(crt_k[-33],title = '인물을 선택하세요')
  
  cha<-crt_k[cn+1]
  
  n_times<-seq(1:length(matthew1))
  
  character_grep <- grepl("예수", matthew1)
  
  w_cnt <- rep(NA, length(n_times))
  
  w_cnt[character_grep] <- 1
  
  plot(w_cnt, xlab='', type="h", ylab='', ylim=c(0,1), yaxt='n', col="skyblue")
  
  par(new=T)
  
  character_grep <- grepl(cha, matthew1)
  
  w_cnt <- rep(NA, length(n_times))
  
  w_cnt[character_grep] <- 1
  
  plot(w_cnt, main=sprintf("예수와 %s의 출현그래프", cha), 
       xlab='', ylab=sprintf("총 %d 회 출현", sum(character_grep)), type="h", ylim=c(0,1), yaxt='n',col="pink4")
  
}

matching_charaters_fun()

# 몇 장에서 나오는지 표시하면 더 좋겠다
## 

###  text 내에 언제, 얼마나 인물 각각 또는 함께 등장하는지

####

matching_charaters_fun <- function(){
  
  graphics.off()
  
  cn <- menu(crt_k,title = "비교할 인물을 선택하세요(두 명까지 가능). 없으면 skip")
  
  crt_k1 <- crt_k[-cn]
  
  cn2 <- menu(c('skip', crt_k1),title = "추가할 인물을 선택하세요")
  
  if (cn2 == 1)
    
    break
  
  cha<-crt_k[cn]
  
  cha2<-crt_k1[cn2-1]
  
  n_times<-seq(1:length(matthew1))
  
  character_grep <- grepl(cha, matthew1)
  
  w_cnt <- rep(NA, length(n_times))
  
  w_cnt[character_grep] <- 1
  
  plot(w_cnt,xlab='',  type="h", ylim=c(0,1), yaxt='n',col="skyblue1")
  
  par(new=T)
  
  character_grep1 <- grepl(cha2, matthew1)
  
  w_cnt <- rep(NA, length(n_times))
  
  w_cnt[character_grep1] <- 1
  
  plot(w_cnt, main=paste(cha, ",", cha2, "그래프"), xlab='', type="h", ylim=c(0,1), yaxt='n',col="pink4")
}

matching_charaters_fun()

### text 내에서 어디에 누가 몇 번 나오는지(분석 전처리를 위한 확인 작업)..

where1<-NULL

for (i in 1:length(crt_k)){
  
  cnt<-length(grep(crt_k[i], matthew1)) # 
  
  where<-grep(crt_k[i], matthew1) # 
  
  where2<-append(where,NULL)
  #where1<-append(where1,values= c(crt_k[i],cnt,where)) #
  
  where1<-append(where1,values= c(crt_k[i],where))
  # where1<-rbind(as.numeric(crt_k[i]),where)
  #print(paste(crt_k[i],cnt))
  #print(where2)
  print(paste(crt_k[i],where2))
}

str(where1)


## 

# 인물과 등장하는 위치 묶기 / 전처리 위한 set 작업
a<-NULL

for (i in 1:length(crt_k)){
  
  cnt<-length(grep(crt_k[i], matthew1)) # 
  
  where<-grep(crt_k[i], matthew1) # 
  
  where2<-append(where,NULL)
  #where1<-append(where1,values= c(crt_k[i],cnt,where)) #
  
  where1<-append(where1,values= c(crt_k[i],where)) # 
  #print(paste(crt_k[i],cnt))
  #print(where2)
  
  a<-as.list(append(a,paste(crt_k[i],where2)))
}


# 등장인물과 등장하는 라인, 데이터 프레임화시켜 구분

character1<-gsub('[0-9]','',a)
line1<-gsub('[^0-9]','',a)

f_data<-cbind(character1,line1)
class(f_data)
str(f_data[,1])

f_data<-data.frame(f_data)

str(f_data)

f_data[,1]<-as.character(f_data[,1])
f_data[,2]<-as.numeric(as.character(f_data[,2])) ## @ 오류 : num로 바로 바꾸면 ''이 1로 바뀌기 때문에 cha -> num.
f_data[is.na(f_data)] <- 0
View(f_data)

# 등장하지 않는 인물은 제거
f_data<-f_data[f_data$line1!=0,]

## 인물 상관관계도를 위한 매트릭스(default=0)

# length(crt_k)
myframe<-matrix(data=0,nrow=length(unique(f_data[,1])), ncol=length(unique(f_data[,1])))
rownames(myframe)<-unique(f_data[,1])
colnames(myframe)<-unique(f_data[,1])
# space<-grep(" ",crt_k)



# 등장인물이 text 내에 +/- 3문장 안에 등장할 경우 동시 등장 빈도수 count +1

for (i in 1:length(f_data[,2])){
  for (j in 1:length(f_data[,2])){
    if (f_data[,1][[i]] == f_data[,1][[j]] & abs(f_data[,2][[i]] != f_data[,2][[j]]) & 
        abs(f_data[,2][[i]] - f_data[,2][[j]]) <=3) #3? 2?
    {
      myframe[f_data[,1][[i]], f_data[,1][[i]]] <- myframe[f_data[,1][[i]], f_data[,1][[i]]] + 1
    }
    else if (f_data[,1][[i]] != f_data[,1][[j]] & abs(f_data[,2][[i]] - f_data[,2][[j]]) <=3 ){
      myframe[f_data[,1][[i]], f_data[,1][[j]]] <- myframe[f_data[,1][[i]], f_data[,1][[j]]] + 1
      myframe[f_data[,1][[i]], f_data[,1][[i]]] <- myframe[f_data[,1][[i]], f_data[,1][[i]]] + 1
    }
  }
}

View(myframe)

# 관계도 그리기
# 시각화를 통한 분석

# install.packages("extrafont")
# install.packages("corrplot")
# install.packages("Hmisc")
# install.packages("networkD3")

library(networkD3)
library(dplyr)

graphics.off()

# 정규화 
normalize <- function(x) {
  return ((x-min(x)) / (max(x) - min(x))) }

myf<-normalize(myframe)

# 
View(myf)

g <- graph.adjacency(myf, weighted=T, mode ="undirected")

g <- simplify(g)
layout1 <- layout.circle(g)
x11()

# 원형 관계 그래프 (선 굵기로 표현)
plot.igraph(g,layout=layout1, edge.width=E(g)$weight*70,
            vertex.size=c(11:11),vertex.label.color=c("red","blue"),vertex.label.cex=c(0.8,0.8))

# str(E(g))

# -1 부터 1 까지 정규화
spatial_normalize <- function(x) {
  return ( 2*(x-min(x)) / (max(x) - min(x))  -1) }

# myf1<-spatial_normalize(myframe)
# View(myf1)
# cor_obj <- cor(myf1)

myframe1<-matrix(data=0,nrow=length(unique(f_data[,1])), ncol=length(unique(f_data[,1])))
rownames(myframe1)<-unique(f_data[,1])
colnames(myframe1)<-unique(f_data[,1])


for (i in 1:length(myframe[1,])){
  myframe1[i,]<- spatial_normalize(myframe[i,])
}

View(myframe1)

cor_obj <- cor(myframe1)
# cor_obj[is.na(cor_obj)] <- -1
View(cor_obj)

# https://cran.r-project.org/web/packages/corrplot/vignettes/corrplot-intro.html

x11()

corrplot(cor_obj, order = "hclust", addrect=4)

# 예상대로 인물 관계에서는 예수가 중심에 있다. 흥미로운 건 다소 언급되지 않는 미세한 관계(부부,천사-악마,사두-바리 등)까지 잡아낸다는 것.
# 미세한 부분을 잡아내지만 한계는 동명이인을 처리 못하는 부분과 드물게 등장하는 인물은 쉽게 함께 등장하는 인물과 클러스터링(상대적인 값)된다.  
# 등장인물 간의 동시 빈도수와 성경 text 내에 일반적으로 추정되는 인물 간의 친밀도는 대체적으로 일치하지만
# 다소 일치하지 않는 부분도 있다. 예컨대, 제자들(실제론 예수와 가깝겠지만) 개개인이 언급되는 건 적어서 다른 외부 인물보단 예수와 멀게 느껴진다.
# 하지만 제자들과의 관계가 높고, 제자 개개인 간의 친밀도는 높게 나와서 이를 감안하면 식별가능하다.
# 위의 한계들은 저자의 배치 의도, 스토리를 통해 말하고자 하는 방식(외부인물을 상대로 제자들은 예수 편이라 언급될 필요가 없기 때문에)과 연관이 깊다.
# 인물간의 4개의 그룹도 만족스럽게 묶인다.

# 한계  1. 친밀도를 나타내는 단어(동사와 형용사)나 '상황'을 파악하진 못한다
#        (반대로, 인물 간의 친밀도에 관심없는 저자가 특정 인물들을 동시에 배치시킨 의도에 주목할 수 있다. 이게 핵심!).
#      2. 인칭대명사를 파악하지 못한다.
