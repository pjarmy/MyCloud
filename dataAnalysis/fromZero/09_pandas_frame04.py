# pandas_DataFrame04

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
# 数据集的横向扩展
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #























