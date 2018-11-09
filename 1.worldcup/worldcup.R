getwd()

setwd("C:/Users/Administrator/Desktop/R")
# 전처리 과정에서는 원데이터를 분석이 가능한 데이터 프레임 구조를 바꾸는 것, 
# 컬럼의 내용을 어떤 로직을 사용해서 추출컬럼으로 변환해야 하는지,
# 세 데이터셋을 통합하여 (데이터수, 컬럼과 형식을 맞추고) 한번에 분석.

# 월드컵 국가, 스코어 데이터
worldcup<-read.csv("WorldCupMatches.csv")

# head(worldcup)
# dim(worldcup)
# sum(is.na(worldcup))

# 총 row 값에 na값으로만 이루어진 rows 포함되어 제거
worldcup<-na.omit(worldcup)

# 컬럼이름 소문자 바꾸기
colnames(worldcup)<-tolower(colnames(worldcup))
# colnames(worldcup)

# 94년 이 전 데이터 제거하기(랭킹데이터와 조인할 테이블 생성)
# View(worldcup)
attach(worldcup)
# dim(worldcup)

#substr(x,1,1)==substr(grep("[A-Za-z]", x, value = T),1,1)
#==substr(grep("[A-Za-z]", win.conditions, value = T),1,5)
#substr(grep("[A-Za-z]", win.conditions, value = T),1,5)==substr(away.team.name,1,5)

# 승리팀 점수주기 위해 승리팀 표기를 위한 로직 (홈,어웨이팀)
worldcup$win <- ifelse( home.team.goals > away.team.goals , 'home',
                        ifelse( home.team.goals < away.team.goals, 'away',
                                ifelse(substr(win.conditions,1,5)==substr(home.team.name,1,5), 'home',
                                       ifelse(substr(win.conditions,1,5)==substr(away.team.name,1,5), 'away', 'draw'))))

# 랭킹 데이터가 1993부터 있어서 1994년 이 후부터 진행
wc_1994<-worldcup[year>=1994,]
# names(wc_1994)

s <- wc_1994[c(8,7,18,20)]
# head(s)
at<-wc_1994[9]

colnames(at)<-colnames(h<-wc_1994[6])

aa<-wc_1994[c(1:5)]
h <- wc_1994[c(1:7,8,18,19,21)]
h <- cbind(h,'home')

# colnames(aa)
# dim(h)
# dim(a)

# rbind를 위해 컬럼을 이름 동일하게
a<-cbind(aa,at,s,wc_1994[21],'away')

colnames(a)[12] <- 'H_A'
colnames(h)[12] <- 'H_A'

colnames(a)[6] <- 'country'
colnames(h)[6] <- 'country'

colnames(a)[7] <- 'goals'
colnames(h)[7] <- 'goals'

colnames(a)[8] <- 'loss'
colnames(h)[8] <- 'loss'

colnames(a)[9] <- 'matchid'
colnames(h)[9] <- 'matchid'

colnames(a)[10] <- 't.init'
colnames(h)[10] <- 't.init'

wc_1994<-rbind(h,a)

# dim(wc_1994)
# View(wc_1994)

# 승,패,무를 컬럼추가
wc_1994$win2[wc_1994$win == 'home' & wc_1994$H_A == 'away'] <- 'lose'
wc_1994$win2[wc_1994$win == 'away' & wc_1994$H_A == 'home'] <- 'lose'
wc_1994$win2[wc_1994$win == 'home' & wc_1994$H_A == 'home'] <- 'win'
wc_1994$win2[wc_1994$win == 'away' & wc_1994$H_A == 'away'] <- 'win'

wc_1994$win2[wc_1994$win == 'draw'] <- 'draw'

#wc_1994 <- colnames(wc_1994)
#wc_1994<-wc_1994[,c(-9,-10)]

# 보기 쉽게 년도, matchid 별 데이터 정렬
head(wc_1994[order(wc_1994$year, decreasing = F),])
wc_1994<-wc_1994[order(wc_1994$year, decreasing = F),]

wc_1994<-wc_1994[order(wc_1994$matchid, decreasing = F),]

# head(wc_1994)

## 조인을 위한 ranking 테이블 정제

# 데이터 설명: 93년 이후 피파 랭킹
rankings<-read.csv("fifa_ranking.csv",header = T)
# View(rankings)
# head(rankings)

colnames(rankings)<-tolower(colnames(rankings))
# colnames(rankings)

# 랭킹 순위 날짜 정제(월드컵 직전)
# str(rankings)
# factor to_Date 
rankings$rank_date<-as.Date(rankings$rank_date)

# 년도 달 정제
# install.packages("lubridate")
library(lubridate)

# 월드컵 년도별 랭킹만 추출 
rankings <- rankings[year(rankings$rank_date)>=1994,]
# unique(rankings$rank_date)
rankings <- rankings[year(rankings$rank_date)%in%c(1994,1998,2002,2006,2010,2014),]

rankings<- rankings[month(rankings$rank_date)%in%c(05,06),]
# unique(rankings$rank_date)

# 월드컵 직전 최종 랭킹 정제
# unique(rankings$rank_date)
rankings<- rankings[!(rankings$rank_date%in%as.Date(c("1994-05-17","2014-05-08"))),]
# unique(rankings$rank_date)

# 필요없는 컬럼 제거
# names(rankings)
# head(rankings)
rnk<-rankings[c(1,2,3,6,16)]
# head(rnk)
colnames(rnk)[3]<-"t.init"
# dim(rnk)
# 두 테이블 조인

# wc_1994 데이터에 정제 불가능한 데이터 유무 확인
wc_1994[!(wc_1994$t.init%in%rnk$t.init),c("t.init")]
unique(wc_1994$t.init)%in%unique(rnk$t.init)

wc<-na.omit(wc_1994)

# 월드컵, 연도별 데이터 정리
# names(wc2014)
wc1994<-wc[wc$year==1994,]
# names(wc[wc$year==1994,])
# View(wc[wc$year==1994,])
wc1998<-wc[wc$year==1998,]
# View(wc[wc$year==1998,])
wc2002<-wc[wc$year==2002,]
wc2006<-wc[wc$year==2006,]
wc2010<-wc[wc$year==2010,]
wc2014<-wc[wc$year==2014,]

rnk1994<-rnk[year(rnk$rank_date)==1994,]
rnk1998<-rnk[year(rnk$rank_date)==1998,]
rnk2002<-rnk[year(rnk$rank_date)==2002,]
rnk2006<-rnk[year(rnk$rank_date)==2006,]
rnk2010<-rnk[year(rnk$rank_date)==2010,]
rnk2014<-rnk[year(rnk$rank_date)==2014,]

# colnames(wc1998)
# colnames(rnk1998)

# 연도별 월드컵 데이터에서 필요한 컬럼과 랭킹 merge
wc1994<-merge(wc1994,rnk1994,by='t.init')[c("year","datetime","stadium","stage",
                                            "matchid","country","t.init",
                                            "rank","goals","loss","win2")]
# dim(wc2014)
# View(wc1994)
wc1998<-merge(wc1998,rnk1998,by='t.init')[c("year","datetime","stadium","stage",
                                            "matchid","country","t.init",
                                            "rank","goals","loss","win2")]

wc2002<-merge(wc2002,rnk2002,by='t.init')[c("year","datetime","stadium","stage",
                                            "matchid","country","t.init",
                                            "rank","goals","loss","win2")]

wc2006<-merge(wc2006,rnk2006,by='t.init')[c("year","datetime","stadium","stage",
                                            "matchid","country","t.init",
                                            "rank","goals","loss","win2")]

wc2010<-merge(wc2010,rnk2010,by='t.init')[c("year","datetime","stadium","stage",
                                            "matchid","country","t.init",
                                            "rank","goals","loss","win2")]

wc2014<-merge(wc2014,rnk2014,by='t.init')[c("year","datetime","stadium","stage",
                                            "matchid","country","t.init",
                                            "rank","goals","loss","win2")]


# 월드컵별 4분위 계수별 등급매기기
summary(wc1994$rank)
wc1994$grade[wc1994$rank<=43]<-'D'
wc1994$grade[wc1994$rank<=27]<-'C'
wc1994$grade[wc1994$rank<=12]<-'B'
wc1994$grade[wc1994$rank<=5]<-'A'

summary(wc1998$rank)
wc1998$grade[wc1998$rank<=74]<-'D'
wc1998$grade[wc1998$rank<=27]<-'C'
wc1998$grade[wc1998$rank<=18]<-'B'
wc1998$grade[wc1998$rank<=8]<-'A'

summary(wc2002$rank)
wc2002$grade[wc2002$rank<=50]<-'D'
wc2002$grade[wc2002$rank<=31]<-'C'
wc2002$grade[wc2002$rank<=20]<-'B'
wc2002$grade[wc2002$rank<=11]<-'A'

summary(wc2006$rank)
wc2006$grade[wc2006$rank<=61]<-'D'
wc2006$grade[wc2006$rank<=35]<-'C'
wc2006$grade[wc2006$rank<=19]<-'B'
wc2006$grade[wc2006$rank<=8]<-'A'

summary(wc2010$rank)
wc2010$grade[wc2010$rank<=105]<-'D'
wc2010$grade[wc2010$rank<=31]<-'C'
wc2010$grade[wc2010$rank<=17]<-'B'
wc2010$grade[wc2010$rank<=6]<-'A'

summary(wc2014$rank)
wc2014$grade[wc2014$rank<=62]<-'D'
wc2014$grade[wc2014$rank<=22]<-'C'
wc2014$grade[wc2014$rank<=14]<-'B'
wc2014$grade[wc2014$rank<=6]<-'A'

m_wc<-rbind(wc1994,wc1998,wc2002,wc2006,wc2010,wc2014)

# 월드컵 데이터 통합

m_wc<-m_wc[order(m_wc$year, decreasing = F),]
m_wc<-m_wc[order(m_wc$matchid, decreasing = F),]


# 등급 factor화시켜 levels 부여 (굳이 안 해도 된다)
#m_wc$grade<-ifelse('group' ,m_wc$grade)
# levels(m_wc$stage)
# unique(m_wc$stage)

#m_wc[m_wc$stage %in% c('Third place','Match for third place','Play-off for third place')]<-
match32 <- grepl('Group',as.character(m_wc$stage))
m_wc$stage2 <- 0
m_wc[match32,'stage2'] <- 32

match16 <- grepl('Round',as.character(m_wc$stage))
m_wc[match16,'stage2'] <- 16

match8 <- grepl('Quarter',as.character(m_wc$stage))
m_wc[match8,'stage2'] <- 8

match4 <- grepl('Semi',as.character(m_wc$stage))
m_wc[match4,'stage2'] <- 4

match2 <- grepl('Final',as.character(m_wc$stage))
m_wc[match2,'stage2'] <- 2

match3 <- grepl('Third', as.character(m_wc$stage))
m_wc[match3,'stage2'] <- 3

match3 <- grepl('Play', as.character(m_wc$stage))
m_wc[match3,'stage2'] <- 3

match3 <- grepl('Match', as.character(m_wc$stage))
m_wc[match3,'stage2'] <- 3

# m_wc<-unique(m_wc)
# x<-as.factor(m_wc$stage2)
# x = factor(x,levels(x)[c(6,5,4,3,2,1)])
# m_wc$stage2<-x

### results 데이터
# 모든 경기결과 홈 어웨이

results<-read.csv("results.csv",header=T)

results<-results[year(as.Date(results$date))>=1990,]
results<-results[year(as.Date(results$date))<=2014 & month(as.Date(results$date))<=05,]

colnames(results)

results$win <- ifelse( results$home_score > results$away_score , 'home', 
                       ifelse( results$home_score < results$away_score, 'away', 'draw'))

h <- results[c(1,2,4,5,8,7,10)]
h<-cbind(h,'home')

a <- results[c(1,3,5,4,8,7,10)]
a<-cbind(a,'away')

# colnames(a)
# colnames(h)

colnames(a)[2] <- 'team'
colnames(h)[2] <- 'team'

colnames(a)[3] <- 'score'
colnames(h)[3] <- 'score'

colnames(a)[4] <- 'loss'
colnames(h)[4] <- 'loss'

colnames(a)[8] <- 'temp'
colnames(h)[8] <- 'temp'

# View(h)
# dim(a)
# View(a)
rs<-rbind(h,a)

# 승,패,무 처리
rs$win2[rs$win == 'home' & rs$temp == 'away'] <- 'lose'
rs$win2[rs$win == 'away' & rs$temp == 'home'] <- 'lose'
rs$win2[rs$win == 'home' & rs$temp == 'home'] <- 'win'
rs$win2[rs$win == 'away' & rs$temp == 'away'] <- 'win'
rs$win2[rs$win == 'draw'] <- 'draw'

# str(rs)
rs<-rs[order(rs$date, decreasing = F),]
rs<-rs[order(rs$city, decreasing = F),]

# tail(rs[order(rs$city),])
# View(rs)

# 결과에 따른 승점 주기
rs$point <- ifelse( rs$win2=='win' , 3, 
                    ifelse( rs$win2=='draw', 1, 0))

# str(rs$date)

rs$date <- substr(as.character(rs$date),1,4)
rs$date<-as.numeric(rs$date)

# 월드컵 직전 4년간 경기 전적
rs$date2 <- ifelse( rs$date>=1990&rs$date<=1994 , 1994, 
                    ifelse( rs$date>1994&rs$date<=1998 , 1998, 
                            ifelse( rs$date>1998&rs$date<=2002 , 2002, 
                                    ifelse( rs$date>2002&rs$date<=2006 , 2006, 
                                            ifelse( rs$date>2006&rs$date<=2010,2010,2014)))))


# 월드컵 직전 1년간 경기 전적
rs$date2 <- ifelse( rs$date>=1993&rs$date<1994 , 1994, 
                    ifelse( rs$date>=1997&rs$date<1998 , 1998, 
                            ifelse( rs$date>=2001&rs$date<2002 , 2002, 
                                    ifelse( rs$date>=2005&rs$date<2006 , 2006, 
                                            ifelse( rs$date>=2009&rs$date<2010,2010,
                                                    ifelse(rs$date>=2013&rs$date<2014,2014,0))))))

rs <- rs[rs$date2!=0,]

View(rs)
View(m_wc)
# m_wc$stage2<-as.numeric(m_wc$stage2)
# m_wc$stage2<-as.numeric(m_wc$stage2)


# 분석단계

library(dplyr)

# tmp 는 월드컵 진출국 중 진출라운드와 랭킹을 4등급으로 매김
# WC_rnk 로 해당국가 최종 진출라운드 표시, 피파랭킹 등급별 표
tmp <- m_wc %>% tbl_df() %>% group_by(country,year) %>% summarise(WC_rnk = min(stage2), fifa_rnk = max(grade))
tmp <- data.frame(tmp)
head(tmp)
View(tmp)

head(rs)

# 월드컵 시기별 피파랭킹과 4(1)년간 전적, 골득실률을 종합
tmp2 <- rs %>% tbl_df() %>% group_by(team,date2) %>% 
  summarise(tot_point = sum(point), tot_score = sum(score), tot_loss = sum(loss), length =length(team))
tmp2 <- data.frame(tmp2)
tmp2$adj_point <- tmp2$tot_point/(tmp2$length*3)
x<-(tmp2$tot_score)/(tmp2$length)
tmp2$adj_score<-((x-min(x))/(max(x)-min(x)))

x1<-(tmp2$tot_loss)/(tmp2$length)
tmp2$adj_loss<-(x1-min(x1))/(max(x1)-min(x1))

View(tmp2)

# 두 테이블을 merge 한 최종 분석테이블
# tmp 테이블로 outer join
tmp3 <- merge(tmp, tmp2, by.x = c('country','year'), by.y =c('team', 'date2'), all.x = T)


tmp3$round <- ifelse( tmp3$WC_rnk == 32, 1 , 
                      ifelse(tmp3$WC_rnk == 16, 2 ,
                             ifelse(tmp3$WC_rnk == 8, 3 ,
                                    ifelse(tmp3$WC_rnk == 4, 4 ,
                                           ifelse(tmp3$WC_rnk == 3, 4 ,
                                                  ifelse(tmp3$WC_rnk == 2,5,0 ))))))

tmp3$fifa_rnk <- ifelse(tmp3$fifa_rnk == 'A', 4,
                        ifelse(tmp3$fifa_rnk== 'B', 3,
                               ifelse(tmp3$fifa_rnk== 'C', 2,
                                      ifelse(tmp3$fifa_rnk== 'D', 1,0))))
# 4년간 전적으로 분석할 때 
summary(tmp3$adj_score)
tmp3$s_rslt <- ifelse(tmp3$adj_score >= 0.26786, 4,
                      ifelse(tmp3$adj_score >= 0.21939, 3,
                             ifelse(tmp3$adj_score >= 0.17460, 2,1)))
summary(tmp3$adj_loss)
tmp3$l_rslt <- ifelse(tmp3$adj_loss <= 0.06512, 4,
                      ifelse(tmp3$adj_loss <= 0.08323, 3,
                             ifelse(tmp3$adj_loss <= 0.09991, 2,1)))
# 4년간 전적으로 분석할 때 
summary(tmp3$adj_score)
tmp3$s_rslt <- ifelse(tmp3$adj_score >= 0.20000, 4,
                      ifelse(tmp3$adj_score >= 0.14286, 3,
                             ifelse(tmp3$adj_score >= 0.09643, 2,1)))
summary(tmp3$adj_loss)
tmp3$l_rslt <- ifelse(tmp3$adj_loss <= 0.03509, 4,
                      ifelse(tmp3$adj_loss <= 0.05614, 3,
                             ifelse(tmp3$adj_loss <= 0.07018, 2,1)))

View(tmp3)

graphics.off()
plot(tmp3$round, tmp3$adj_point )                             
plot(tmp3$round, tmp3$fifa_rnk )

tmp4 <- na.omit(tmp3)
tmp3$l_rslt

View(tmp4)
colnames(tmp3)

lm(round ~ fifa_rnk  , data = tmp4 )
lm(round ~ adj_score  , data = tmp4 )
lm(round ~ l_rslt  , data = tmp4 )
lm(round ~ s_rslt  , data = tmp4 )
lm(round ~ fifa_rnk + adj_score  , data = tmp4 )
lm(round ~ fifa_rnk + l_rslt  , data = tmp4 )
lm(round ~ fifa_rnk + s_rslt  , data = tmp4 )

plot(tmp4$round,tmp4$adj_point)
plot(tmp4$round,tmp4$adj_score)
plot(tmp4$round,tmp4$fifa_rnk)
plot(tmp4$round,tmp4$l_rslt)
plot(tmp4$round,tmp4$s_rslt)

cor(tmp4$round,tmp4$adj_point)
cor(tmp4$round,tmp4$adj_score)
cor(tmp4$round,tmp4$fifa_rnk)
cor(tmp4$round,tmp4$l_rslt)
cor(tmp4$round,tmp4$s_rslt)


cor(tmp4$fifa_rnk,tmp4$adj_point)
cor(tmp4$fifa_rnk,tmp4$l_rslt)
cor(tmp4$fifa_rnk,tmp4$s_rslt)
cor(tmp4$l_rslt,tmp4$s_rslt)


fit1 <- lm(round ~ s_rslt + l_rslt, data = tmp3 )
fit1

fit2 <- lm(round ~ s_rslt + l_rslt + adj_score, data = tmp3)
fit2

fit3 <- lm(round ~  fifa_rnk + s_rslt + l_rslt + adj_score, data = tmp3 )
fit3

fit4 <- lm(round ~  fifa_rnk+adj_point , data = tmp3 )
fit4

fit5 <- lm(round ~  fifa_rnk , data = tmp3 )

summary(fit1)
summary(fit2)
summary(fit3)
summary(fit4)
summary(fit5)
write.csv(tmp4,"worldcupdata.csv")

#### 회귀곡선 그리기

lm(round ~  fifa_rnk + adj_score, data = tmp3 )



## 3d plot 

#install.packages("plotly")
library(plotly)
packageVersion('plotly')

p <- plot_ly(tmp3, x = ~fifa_rnk, y = ~round, z = ~adj_score, 
             color = ~fifa_rnk, colors = c('blue1', 'red2','green3','yellow4')) %>%
  add_markers() %>%
  layout(scene = list(xaxis = list(title = 'fifa_rank'),
                      yaxis = list(title = 'round'),
                      zaxis = list(title = 'adj_score')))
# x11()
p


# 결국 월드컵 (진출)결과에 대하여 골득실률, 월드컵 직전 1년간 경기 결과에 따른 승점, 피파랭킹 가운데 
# 피파랭킹만이 그나마(낮은 p값 한해서) 유의미한 변수다.
# Multiple R-squared:  0.1944,	Adjusted R-squared:   0.19 
# F-statistic: 44.17 on 1 and 183 DF,  p-value: 3.352e-10
# 피파랭킹은 p-value 3.352e-10 에 한해서 월드컵 결과에  19% 정도 설명력을 지닌다.
# 하지만 외부결과데이터만으로는 결과 예측을 하기 힘든 것으로 보인다.
# 경기 내부 데이터(패스성공률, 유효슈팅, 전술 등등)이 필요할 것 같다. 
# 하지만 외부데이터로 새로 시도해 볼 수 있는 추출변수는 상대전적(?)(=대진운?)이 있을 것이다.