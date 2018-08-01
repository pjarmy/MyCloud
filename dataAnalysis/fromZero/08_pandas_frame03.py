# pandas_DataFrame03
# E:/Documents/GitHub/MyCloud/dataAnalysis/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 频数统计
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 读数据
import pandas as pd
income = pd.read_excel('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/pandas_income.xlsx')

# 数据的前 5行
income.head()

===============================================================
   age  edu time  gender  zcjz  zcss  week hours income level
0   39        13    Male  2174     0          40        <=50K
1   50        13    Male     0     0          13        <=50K
2   38         9    Male     0     0          40        <=50K
3   53         7    Male     0     0          40        <=50K
4   28        13  Female     0     0          40        <=50K
===============================================================

# 频数统计，统计某个离散变量各水平的频次
income.gender.value_counts()

===============================
Female    127
Male      117
Name: gender, dtype: int64
===============================

income.gender.value_counts()/sum(income.gender.value_counts())

===============================
Female    0.520492
Male      0.479508
Name: gender, dtype: float64
===============================

# R
# library('readxl')
# income <- read_excel('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/pandas_income.xlsx')
# head(income)
#
# ===================================================================
# # A tibble: 6 x 7
#     age `edu time` gender  zcjz  zcss `week hours` `income level`
#   <dbl>      <dbl> <chr>  <dbl> <dbl>        <dbl> <chr>
# 1    39         13 Male    2174     0           40 <=50K
# 2    50         13 Male       0     0           13 <=50K
# 3    38          9 Male       0     0           40 <=50K
# 4    53          7 Male       0     0           40 <=50K
# 5    28         13 Female     0     0           40 <=50K
# 6    49         21 Female     0     0           10 <=50K
# ===================================================================
#
# table(income$gender)
#
# =================
# Female   Male
#    127    117
# =================
#
# prop.table(table(income$gender))
#
# =======================
#    Female      Male
# 0.5204918 0.4795082
# =======================



# 统计两个离散变量的交叉统计表，crosstab()

pd.crosstab(index=income.gender, columns=income['income level'])

==============================
income level  <=50K  >=50K
gender
Female           72     55
Male             52     65
==============================

# R
# table(income$gender, income$`income level`)
#
# =========================
#          <=50K >=50K
#   Female    72    55
#   Male      52    65
# =========================



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 缺失值处理
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# 缺失值可以通过删除和替补处理
# 监控变量是否存在缺失值，isnull(), dropna(), fillna()

# 首先，我们手工编造一个含缺失值的数据框
# 导入第三方模块
import pandas as pd
import numpy as np

# 构建数据集
df = pd.DataFrame([[1,2,3,4],
                    [np.NaN,6,7,np.NaN],
                    [11,np.NaN,12,13],
                    [100,200,300,400],
                    [20,40,60,np.NaN]], columns=['x1','x2','x3','x4'])
df

===============================
      x1     x2   x3     x4
0    1.0    2.0    3    4.0
1    NaN    6.0    7    NaN
2   11.0    NaN   12   13.0
3  100.0  200.0  300  400.0
4   20.0   40.0   60    NaN
===============================

# 其次，使用isnull()检查数据集的缺失状况
print(any(df.isnull()), '\n')

# 每一列是否有缺失，及缺失比例
is_null = []
null_ratio = []
for col in df.columns:
    is_null.append(any(pd.isnull(df[col])))
    null_ratio.append(float(round(sum(pd.isnull(df[col]))/df.shape[0],2)))
print(is_null, '\n', null_ratio, '\n')

# 每一行是否有缺失
is_null = []
for index in list(df.index):
    is_null.append(any(pd.isnull(df.iloc[index,:])))
print(is_null, '\n')

=====================================
True

[True, True, False, True]
 [0.2, 0.2, 0.0, 0.4]

[False, True, True, False, True]
=====================================


# 最后，对缺失数据进行处理
# 删除法，dropna(), 对含有缺失的行（任意一列）进行删除，删除那些全是缺失（所有列）的行

# 删除任何含缺失的观测
df.dropna()

==============================
      x1     x2   x3     x4
0    1.0    2.0    3    4.0
3  100.0  200.0  300  400.0
==============================

# 删除每行中所有变量都为缺失的观测
df.dropna(how='all')

==============================
      x1     x2   x3     x4
0    1.0    2.0    3    4.0
1    NaN    6.0    7    NaN
2   11.0    NaN   12   13.0
3  100.0  200.0  300  400.0
4   20.0   40.0   60    NaN
==============================


# 替补法
fillna()提供前后替补、后向替补和函数替补的几种方法

 # 前向替补
 df.fillna(method='ffill')

==============================
      x1     x2   x3     x4
0    1.0    2.0    3    4.0
1    1.0    6.0    7    4.0
2   11.0    6.0   12   13.0
3  100.0  200.0  300  400.0
4   20.0   40.0   60  400.0
==============================


# 后向替补

df.fillna(method='bfill')

==============================
      x1     x2   x3     x4
0    1.0    2.0    3    4.0
1   11.0    6.0    7   13.0
2   11.0  200.0   12   13.0
3  100.0  200.0  300  400.0
4   20.0   40.0   60    NaN
==============================


# 不同的列用不同的函数替补
df.fillna(value = {'x1':df.x1.mean(),
                    'x2':df.x2.median(),
                    'x4':df.x4.max()})

==============================
      x1     x2   x3     x4
0    1.0    2.0    3    4.0
1   33.0    6.0    7  400.0
2   11.0   23.0   12   13.0
3  100.0  200.0  300  400.0
4   20.0   40.0   60  400.0
==============================


# R
# df <- data.frame(x1 = c(1,NA,11,100,20),
#                 x2 = c(2,6,NA,200,40),
#                 x3 = c(3,7,212,300,60),
#                 x4 = c(4,NA,13,400,NA))
# df
#
# ====================
#    x1  x2  x3  x4
# 1   1   2   3   4
# 2  NA   6   7  NA
# 3  11  NA 212  13
# 4 100 200 300 400
# 5  20  40  60  NA
# ====================
#
# # 总览数据集是否存在缺失
# any(is.na(df))
#
# ===============
# [1] TRUE
# ===============
#
# # 每一列是否有缺失，及缺失比例
# is_null = NULL
# null_ratio = NULL
# for (col in names(df)){
#     is_null = c(is_null, any(is.na(df[,col])))
#     null_ratio = c(null_ratio,sum(is.na(df[,col]))/dim(df)[1])
# }
#
# is_null
#
# ==============================
# [1]  TRUE  TRUE FALSE  TRUE
# ==============================
#
# null_ratio
#
# =========================
# [1] 0.2 0.2 0.0 0.4
# =========================
#
#
# is_null = NULL
#
# for (row in 1:nrow(df)){
#     is_null = c(is_null,any(is.na(df[row,])))
# }
#
# is_null
#
# # 或者
# !complete.cases(df)
#
# ====================================
# [1] FALSE  TRUE  TRUE FALSE  TRUE
# ====================================
#
#
# # 删除任何含缺失的观测
# na.omit(df)
#
# =======================
#    x1  x2  x3  x4
# 1   1   2   3   4
# 4 100 200 300 400
# =======================
#
#
# # R中没有删除每行元素都是缺失的观测，但可以自定义函数
# df = data.frame(x = c(1,2,NA,NA),
#                 y = c(NA,5,NA,NA))
# df
#
# ==========
#    x  y
# 1  1 NA
# 2  2  5
# 3 NA NA
# 4 NA NA
# ==========
#
# move.all.na <- function(data) {
#     is.na.row = NULL
#     for (row in 1:nrow(data)){
#         is.na.row = c(is.na.row, all(is.na(data[row,])))
#     }
#     return(data[!is.na.row,])
# }
#
# move.all.na(df)
#
# ==========
#   x  y
# 1 1 NA
# 2 2  5
# ==========
#
#
# # 缺失值替补，使用Hmisc包中的impute()
# df
# # install.packages('Hmisc')
# library(Hmisc)
# df$x1 <- impute(df$x1, mean)
#
# ===================
#    x1  x2  x3  x4
# 1   1   2   3   4
# 2  33   6   7  NA
# 3  11  NA 212  13
# 4 100 200 300 400
# 5  20  40  60  NA
# ===================
#
# df$x2 <- impute(df$x2, median)
#
# ====================
#    x1  x2  x3  x4
# 1   1   2   3   4
# 2  33   6   7  NA
# 3  11  23 212  13
# 4 100 200 300 400
# 5  20  40  60  NA
# ====================
#
# df$x4 <- impute(df$x4,max)
# df
#
# ====================
#    x1  x2  x3  x4
# 1   1   2   3   4
# 2  33   6   7 400
# 3  11  23 212  13
# 4 100 200 300 400
# 5  20  40  60 400
# ====================



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 数据映射
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Python和 R 在做循环时，效率还是很低的，如何避免循环达到相同的效果呢
# 研究映射函数 apply()，将用户指定的函数运用到数据集的纵轴即各个变量或横轴即各个行


# 总览数据集是否存在缺失
print(any(df.isnull()), '\n')

# 每一列是否有缺失，及缺失比例
is_null = []
null_ratio = []
for col in df.columns:
    is_null.append(any(pd.isnull(df[col])))
    null_ratio.append(float(round(sum(pd.isnull(df[col]))/df.shape[0],2)))
print(is_null, '\n', null_ratio, '\n')

# 每一行是否有缺失
is_null = []
for index in list(df.index):
    is_null.append(any(pd.isnull(df.iloc[index:1])))
print(is_null, '\n')

==================================
True

[True, True, False, True]
 [0.2, 0.2, 0.0, 0.4]

[True, True, True, True, True]
==================================


# 通过映射函数可以简洁而快速的实现

# 查看各列和各行是否有缺失
# 创建一个判断对象是否含缺失的匿名函数
is_null = lambda x : any(pd.isnull(x))

# 使用 apply() 映射函数
# axis=0 表示将 is_null 函数映射到各列
df.apply(func = is_null, axis = 0)

=============
x1     True
x2     True
x3    False
x4     True
dtype: bool
=============


# axis=1表示将 is_null 函数映射到各行
df.apply(func = is_null, axis = 1)

=============
0    False
1     True
2     True
3    False
4     True
dtype: bool
=============


# 计算每个学生的总成绩，或各科平均分，可以使用 apply()

# 读取数据
score = pd.read_csv('E:/Documents/GitHub/MyCloud/dataAnalysis/fromZero/data/pandas_training.csv')
score.head()

=============================================
    STG   SCG   STR   LPR   PEG       UNS
0  0.00  0.00  0.00  0.00  0.00  very_low
1  0.08  0.08  0.10  0.24  0.90      High
2  0.06  0.06  0.05  0.25  0.33       Low
3  0.85  0.67  0.60  0.45  0.14  very_low
4  0.41  0.42  0.23  0.25  0.34    Middle
=============================================
 
# 每个学生的平均成绩
score['tot'] = score.iloc[:,0:5].apply(func = np.sum, axis=1)

==================================================
    STG   SCG   STR   LPR   PEG       UNS   tot
0  0.00  0.00  0.00  0.00  0.00  very_low  0.00
1  0.08  0.08  0.10  0.24  0.90      High  1.40
2  0.06  0.06  0.05  0.25  0.33       Low  0.75
3  0.85  0.67  0.60  0.45  0.14  very_low  2.71
4  0.41  0.42  0.23  0.25  0.34    Middle  1.65
==================================================

# 每门学科的平均分数
score.iloc[:,0:5].apply(func = np.mean, axis=0)

==================
STG    0.507889
SCG    0.481156
STR    0.509447
LPR    0.487035
PEG    0.462211
dtype: float64
==================


# # # R
# # # 实现上述映射操作的函数有很多，这里 sapply()和 apply()两个函数

# # 统计每列是否存在缺失
# sapply(df, function(x) any(is.na(x)))

# ==========================
   # x1    x2    x3    x4 
 # TRUE  TRUE FALSE  TRUE
# ==========================

# # 读取数据
# score <- read.csv('E:/Documents/GitHub/MyCloud/dataAnalysis/fromZero/data/pandas_training.csv')

# # 每个学生的总成绩
# score$tot <- apply(as.matrix(score[,1:5]),1,sum)

# head(score, 3)

# =============================================
   # STG  SCG  STR  LPR  PEG      UNS  tot
# 1 0.00 0.00 0.00 0.00 0.00 very_low 0.00
# 2 0.08 0.08 0.10 0.24 0.90     High 1.40
# 3 0.06 0.06 0.05 0.25 0.33      Low 0.75
# =============================================

# # 每门科目的平均分数
# sapply(score[,1:5],mean)

# ====================================================
      # STG       SCG       STR       LPR       PEG 
# 0.5078894 0.4811558 0.5094472 0.4870352 0.4622111
# ====================================================

# 如果需要统计数据集每行的某个值，需要先将数值型的数据框转化为矩阵，然后给予矩阵使用apply()



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 数据汇总
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


income = pd.read_excel('E:/Documents/GitHub/MyCloud/dataAnalysis/fromZero/data/pandas_income.xlsx')
income.head(3)

===============================================================
   age  edu time gender  zcjz  zcss  week hours income level
0   39        13   Male  2174     0          40        <=50K
1   50        13   Male     0     0          13        <=50K
2   38         9   Male     0     0          40        <=50K
===============================================================

# 对性别 gender 做分组统计
groupby_gender = income.groupby(['gender'])
groupby_gender.aggregate(np.mean)

=============================================================
              age   edu time       zcjz  zcss  week hours
gender
Female  44.102362  19.771654   0.000000   0.0   24.905512
Male    41.700855  18.752137  18.581197   0.0   25.666667
=============================================================

# 对性别 gender 和收入水平两个变量做分组统计
grouped = income.groupby(['gender','income level'])
grouped.aggregate(np.mean)

=========================================================================
                           age   edu time       zcjz  zcss  week hours
gender income level
Female <=50K         44.597222  19.875000   0.000000   0.0   25.000000
       >=50K         43.454545  19.636364   0.000000   0.0   24.781818
Male   <=50K         42.942308  18.423077  41.807692   0.0   26.903846
       >=50K         40.707692  19.015385   0.000000   0.0   24.676923
=========================================================================

# 对性别和收入水平两个变量做分组统计，但不同的变量作不同的聚合
grouped = income.groupby(['gender','income level'])
# 例如，对年龄算平均值，对教育时长算中位数
grouped.aggregate({'age':np.mean, 'edu time':np.median})

===========================================
                           age  edu time
gender income level
Female <=50K         44.597222      17.0
       >=50K         43.454545      18.0
Male   <=50K         42.942308      14.5
       >=50K         40.707692      15.0
===========================================


# R
# head(income,3)

# ======================================================
# # A tibble: 3 x 7
    # age `edu time` gender  zcjz  zcss `week hours`
  # <dbl>      <dbl> <chr>  <dbl> <dbl>        <dbl>
# 1    39         13 Male    2174     0           40
# 2    50         13 Male       0     0           13
# 3    38          9 Male       0     0           40
# # ... with 1 more variable: `income level` <chr>
# ======================================================

# # install.packages('dplyr')
# library(dplyr)

# # 对性别变量分组
# groupby.gender <- group_by(.data = income, gender)

# # 需要对什么变量汇总，就需要手工书写
# summarise(groupby.gender, avg.age = mean(age), avg.edu_time = mean(`edu time`))

# ===================================
# # A tibble: 2 x 3
  # gender avg.age avg.edu_time
  # <chr>    <dbl>        <dbl>
# 1 Female    44.1         19.8
# 2 Male      41.7         18.8
# ===================================

# # 对性别和收入水平分组
# grouped <- group_by(.data = income, gender, `income level`)
# summarise(grouped, avg.age = mean(age), median.edu_time = median(`edu time`))

# ====================================================
# # A tibble: 4 x 4
# # Groups:   gender [?]
  # gender `income level` avg.age median.edu_time
  # <chr>  <chr>            <dbl>           <dbl>
# 1 Female <=50K             44.6            17  
# 2 Female >=50K             43.5            18  
# 3 Male   <=50K             42.9            14.5
# 4 Male   >=50K             40.7            15
# ====================================================
















