# pandas_DataFrame04
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 数据集的纵向合并
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os
import pandas as pd
from pandas import *

# 指定数据文件所在路径
path = 'F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/data1/'
# 罗列路径下的文件名称
filenames = os.listdir(path)
# 通过 for循环完成数据的堆叠
dataframes = []
for file in filenames:
	dataframes.append(pd.read_excel(path + file))
alldata = pd.concat(dataframes, ignore_index=True)

alldata.head()

=============================
   id    name gender  age
0   1  4w261Y      M   39
1   2  20FiY7      M   50
2   3  vBJVJi      M   38
3   4  637A6J      M   53
4   5  pVoeO3      F   28
=============================


# R
# # 加载读取excel文件的包
# library(readxl)

# # 设置工作空间
# setwd('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/data1')

# # 读取工作空间中的文件名
# filenames <- dir()

# # for循环完成数据的读取和堆叠
# alldata <- data.frame()
# for (file in filenames){
	# data = read_excel(file)
	# alldata = rbind(alldata, data)
# }

# head(alldata)

# ==============================
# # A tibble: 6 x 4
     # id name   gender   age
  # <dbl> <chr>  <chr>  <dbl>
# 1     1 4w261Y M         39
# 2     2 20FiY7 M         50
# 3     3 vBJVJi M         38
# 4     4 637A6J M         53
# 5     5 pVoeO3 F         28
# 6     6 r187u6 F         49
# ==============================



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 数据集的横向扩展
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

user_info = pd.read_excel('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/data2/pandas_user_info.xlsx')
user_info.head()

======================
     id gender  age
0  9192      F   19
1  6415      F   26
2  4767      M   23
3  1214      M   19
4  8952      M   24
======================

economy_info = pd.read_excel('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/data2/pandas_economy_info.xlsx')
economy_info.head()

===========================
     id  income  outcome
0  9351   12000      739
1  5886    4000     1876
2  1073    9000      524
3  6533   10000      949
4  1684   10000      881
===========================


# # merge()连接两个数据集
# pd.merge(left, right, how='inner', on= None, left_on=None, right_on=None,
		# left_index=False, right_index=False, sort=False,
		# suffixes=('_x','_y'), coyp=True, indicator=False)

# left,right: 为需要连接的两张表；
# how: 默认对两张表进行内连，'right','left'为右连和左连，一般inner和left使用最多；
# on: 指定关联两张表的公共字段；
# left_on,right_on: 质量left表和right表中需要关联的字段
# left_index,right_index: 指定left表和right表中需要关联的行索引

# 两个数据集的连接
merge_data = pd.merge(user_info, economy_info, how='left')
merge_data.head()

=========================================
     id gender  age   income  outcome
0  9192      F   19   5000.0   1071.0
1  6415      F   26   9000.0   1682.0
2  4767      M   23   5000.0   1375.0
3  1214      M   19   8000.0   1310.0
4  8952      M   24  11000.0   1721.0
=========================================

# # 如果关联字段不一致，则需要left_on和right_on了

# 修改字段的名称
user_info = user_info.rename(columns = {'id':'Id'})
# 指定连接的字段
merge_data2 = pd.merge(user_info, economy_info, how='left', left_on='Id', right_on ='id')
merge_data2.head()

==================================================
     Id gender  age      id   income  outcome
0  9192      F   19  9192.0   5000.0   1071.0
1  6415      F   26  6415.0   9000.0   1682.0
2  4767      M   23  4767.0   5000.0   1375.0
3  1214      M   19  1214.0   8000.0   1310.0
4  8952      M   24  8952.0  11000.0   1721.0
==================================================

# 并不修改merge_data2
merge_data2.drop('id', axis=1).head()

========================================
     Id gender  age   income  outcome
0  9192      F   19   5000.0   1071.0
1  6415      F   26   9000.0   1682.0
2  4767      M   23   5000.0   1375.0
3  1214      M   19   8000.0   1310.0
4  8952      M   24  11000.0   1721.0
========================================


# # R
# # 读取数据
# user_info <- read.csv('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/data2/pandas_user_info.csv')
# economy_info <- read.csv('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/data2/pandas_economy_info.csv')

# # 加载dplyr包
# library(dplyr)
# # left_join函数
# data_all <- left_join(user_info, economy_info)
# head(data_all)

# =====================================
    # id gender age income outcome
# 1 9192      F  19   5000    1071
# 2 6415      F  26   9000    1682
# 3 4767      M  23   5000    1375
# 4 1214      M  19   8000    1310
# 5 8952      M  24  11000    1721
# 6 2980      F  20     NA      NA
# =====================================

# # 变量重命名
# user_info2 <- rename(user_info, Id = id)
# head(user_info2)

# ====================
    # Id gender age
# 1 9192      F  19
# 2 6415      F  26
# 3 4767      M  23
# 4 1214      M  19
# 5 8952      M  24
# 6 2980      F  20
# ====================

# # 数据连接
# data_all2 <- left_join(user_info2, economy_info, by = c('Id'='id'))
# head(data_all2)

# ====================================
    # Id gender age income outcome
# 1 9192      F  19   5000    1071
# 2 6415      F  26   9000    1682
# 3 4767      M  23   5000    1375
# 4 1214      M  19   8000    1310
# 5 8952      M  24  11000    1721
# 6 2980      F  20     NA      NA
# ====================================



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 离散变量的哑变量处理
# pd.get_dummies()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import pandas as pd
# 数据读取
user_level = pd.read_csv('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/pandas_user_level.csv')
user_level.head()

==========================
   id gender  age level
0   1      F   25    V1
1   2      M   26    V1
2   3      F   20    V2
3   4      M   25    V2
4   5      M   20    V1
==========================

# 哑变量处理
user_level_dummy = pd.get_dummies(user_level, columns = ['gender','level']).head()

==========================================================================
   id  age  gender_F  gender_M  level_V1  level_V2  level_V3  level_V4
0   1   25         1         0         1         0         0         0
1   2   26         0         1         1         0         0         0
2   3   20         1         0         0         1         0         0
3   4   25         0         1         0         1         0         0
4   5   20         0         1         1         0         0         0
==========================================================================

# 建模时要删除原离散变量中的某一个水平，作为参照组
user_level_dummy = pd.get_dummies(user_level, columns = ['gender','level']).head()
user_level_dummy.drop(['gender_F','level_V1'], axis = 1).head()

======================================================
   id  age  gender_M  level_V2  level_V3  level_V4
0   1   25         0         0         0         0
1   2   26         1         0         0         0
2   3   20         0         1         0         0
3   4   25         1         1         0         0
4   5   20         1         0         0         0
======================================================


# # R
# # dummyVars()
# # install.packages('caret')

# # 数据读取
# user_level <- read.csv('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/pandas_user_level.csv')
# str(user_level)

# # 取出索引因子型变量
# factor_vars <- names(user_level)[sapply(user_level, class) == 'factor']
# factor_vars

# =======================
# [1] "gender" "level"
# =======================

# # 构建离散变量的公式
# f <- formula(paste0('~', paste(factor_vars, collapse = '+')))
# # 使用dummyVars函数创建哑变量
# dummy <- dummyVars(f, data = user_level)
# # 哑变量输出
# head(predict(dummy, user_level))

# ===========================================================
  # gender.F gender.M level.V1 level.V2 level.V3 level.V4
# 1        1        0        1        0        0        0
# 2        0        1        1        0        0        0
# 3        1        0        0        1        0        0
# 4        0        1        0        1        0        0
# 5        0        1        1        0        0        0
# 6        1        0        1        0        0        0
# ===========================================================

# str(user_level)

# =============================================================================
# 'data.frame':	154 obs. of  4 variables:
 # $ id    : int  1 2 3 4 5 6 7 8 9 10 ...
 # $ gender: Factor w/ 2 levels "F","M": 1 2 1 2 2 1 1 1 2 2 ...
 # $ age   : int  25 26 20 25 20 37 34 20 22 35 ...
 # $ level : Factor w/ 4 levels "V1","V2","V3",..: 1 1 2 2 1 1 4 3 4 2 ...
 # =============================================================================

# # 通过 cbind() 将 id、age 两个数据集合并起来
# data <- cbind(subset(user_level, select = -c(gender,level)),
				# data.frame(predict(dummy, user_level)))
# head(data)

# ==================================================================
  # id age gender.F gender.M level.V1 level.V2 level.V3 level.V4
# 1  1  25        1        0        1        0        0        0
# 2  2  26        0        1        1        0        0        0
# 3  3  20        1        0        0        1        0        0
# 4  4  25        0        1        0        1        0        0
# 5  5  20        0        1        1        0        0        0
# 6  6  37        1        0        1        0        0        0
# ==================================================================

# data <- data[,-c(3,5)]
# head(data)

# ===============================================
  # id age gender.M level.V2 level.V3 level.V4
# 1  1  25        0        0        0        0
# 2  2  26        1        0        0        0
# 3  3  20        0        1        0        0
# 4  4  25        1        1        0        0
# 5  5  20        1        0        0        0
# 6  6  37        0        0        0        0
# ===============================================



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 连续变量的分段
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import numpy as np
import pandas as pd

# 随机生成一个表示年龄的字段
age = np.random.randint(low = 12, high = 80, size = 1000)
age = pd.Series(age)
age.describe()

======================
count    1000.000000
mean       46.627000
std        19.302654
min        12.000000
25%        30.000000
50%        47.500000
75%        63.000000
max        79.000000
dtype: float64
======================


# 18~45 青年、45~60 中年、60~ 老年
# 数据切割
age_cut = pd.cut(age, bins = [0,18,45,60,80], right = False,
				labels = ['未成年','青年','中年','老年'])
age_cut.head()

=========================================================
0    老年
1    老年
2    青年
3    老年
4    青年
dtype: category
Categories (4, object): [未成年 < 青年 < 中年 < 老年]
=========================================================

# right: False 表示分段的数据区间不包含上限

age.head(5)            # 原始年龄

===============
0    75
1    74
2    18
3    73
4    28
dtype: int32
===============


# # R
# # 加载第三方包
# library(Hmisc)
# # 随机生成年龄数据
# age <- round(runif(n = 1000, min = 12, max = 80), 0)
# # 年龄分段
# age_cut <- cut2(age, cuts = c(18,45,60))
# head(age_cut)

# ======================================================
# [1] [12,18) [18,45) [18,45) [60,80] [18,45) [18,45)
# Levels: [12,18) [18,45) [45,60) [60,80]
# ======================================================

# # 设置标签
# cuts <- factor(age_cut, levels = c('[12,18)','[18,45)','[45,60)','[60,80]'),
				# labels = c('未成年','青年','中年','老年'))
# head(cuts)

# ======================================================
# [1] 未成年 青年   青年   老年   青年   青年
# Levels: 未成年 青年 中年 老年
# ======================================================

# head(age)

# ========================
# [1] 16 30 41 78 24 30
# ========================
