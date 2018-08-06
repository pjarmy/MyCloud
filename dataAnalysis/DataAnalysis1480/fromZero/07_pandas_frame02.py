# pandas_DataFrame02
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

# 借助 pandas模块进行数据的预处理
# 内容包括数据集变量与观测的筛选、变量的重命名、数据类型的变换、排序、重复观测的删除、和数据集的抽样



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 数据筛选
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import pandas as pd
iris = pd.read_csv('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/pandas_iris.csv')
iris.head()

==================================================================
   SepalLength  SepalWidth  PetalLength  PetalWidth         Name
0          5.1         3.5          1.4         0.2  Iris-setosa
1          4.9         3.0          1.4         0.2  Iris-setosa
2          4.7         3.2          1.3         0.2  Iris-setosa
3          4.6         3.1          1.5         0.2  Iris-setosa
4          5.0         3.6          1.4         0.2  Iris-setosa
==================================================================


# 在 pandas取出一列：
#     名称索引法
#     点取法

# 取出 Name列
# 名称索引法
iris['Name'].head()

# 点取法
iris.Name.head()

=============================
0    Iris-setosa
1    Iris-setosa
2    Iris-setosa
3    Iris-setosa
4    Iris-setosa
Name: Name, dtype: object
=============================

# R
# iris <- read.csv('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/pandas_iris.csv')
# head(iris)
#
# =============================================================
#   SepalLength SepalWidth PetalLength PetalWidth        Name
# 1         5.1        3.5         1.4        0.2 Iris-setosa
# 2         4.9        3.0         1.4        0.2 Iris-setosa
# 3         4.7        3.2         1.3        0.2 Iris-setosa
# 4         4.6        3.1         1.5        0.2 Iris-setosa
# 5         5.0        3.6         1.4        0.2 Iris-setosa
# 6         5.4        3.9         1.7        0.4 Iris-setosa
# =============================================================
#
# head(iris[,"Name"])
# head(iris$Name)
#
# ===============================================================================
# [1] Iris-setosa Iris-setosa Iris-setosa Iris-setosa Iris-setosa Iris-setosa
# Levels: Iris-setosa Iris-versicolor Iris-virginica
# ===============================================================================


# 一个变量的观测筛选
# 取出'Iris-setosa'花种
iris.loc[iris.Name=='Iris-setosa',:].head()

==================================================================
   SepalLength  SepalWidth  PetalLength  PetalWidth         Name
0          5.1         3.5          1.4         0.2  Iris-setosa
1          4.9         3.0          1.4         0.2  Iris-setosa
2          4.7         3.2          1.3         0.2  Iris-setosa
3          4.6         3.1          1.5         0.2  Iris-setosa
4          5.0         3.6          1.4         0.2  Iris-setosa
==================================================================

# 两个变量的观测筛选
# 取出 Iris-setosa花种，且SepalLength大于 5的观测值
iris.loc[(iris.Name=='Iris-setosa') & (iris['SepalLength']>5),:]

====================================================================
    SepalLength  SepalWidth  PetalLength  PetalWidth         Name
0           5.1         3.5          1.4         0.2  Iris-setosa
5           5.4         3.9          1.7         0.4  Iris-setosa
10          5.4         3.7          1.5         0.2  Iris-setosa
14          5.8         4.0          1.2         0.2  Iris-setosa
15          5.7         4.4          1.5         0.4  Iris-setosa
16          5.4         3.9          1.3         0.4  Iris-setosa
17          5.1         3.5          1.4         0.3  Iris-setosa
18          5.7         3.8          1.7         0.3  Iris-setosa
19          5.1         3.8          1.5         0.3  Iris-setosa
20          5.4         3.4          1.7         0.2  Iris-setosa
21          5.1         3.7          1.5         0.4  Iris-setosa
23          5.1         3.3          1.7         0.5  Iris-setosa
27          5.2         3.5          1.5         0.2  Iris-setosa
28          5.2         3.4          1.4         0.2  Iris-setosa
31          5.4         3.4          1.5         0.4  Iris-setosa
32          5.2         4.1          1.5         0.1  Iris-setosa
33          5.5         4.2          1.4         0.2  Iris-setosa
36          5.5         3.5          1.3         0.2  Iris-setosa
39          5.1         3.4          1.5         0.2  Iris-setosa
44          5.1         3.8          1.9         0.4  Iris-setosa
46          5.1         3.8          1.6         0.2  Iris-setosa
48          5.3         3.7          1.5         0.2  Iris-setosa
====================================================================

# 两个变量的观测筛选并筛选部分变量
# 取出 Iris-setosa花种，且SepalLength大于 5的观测值
# 且只保留SepalLength和SepalWidth变量
iris.loc[(iris.Name=='Iris-setosa') & (iris['SepalLength']>5), ['SepalWidth','SepalWidth']]

============================
    SepalWidth  SepalWidth
0          3.5         3.5
5          3.9         3.9
10         3.7         3.7
14         4.0         4.0
15         4.4         4.4
16         3.9         3.9
17         3.5         3.5
18         3.8         3.8
19         3.8         3.8
20         3.4         3.4
21         3.7         3.7
23         3.3         3.3
27         3.5         3.5
28         3.4         3.4
31         3.4         3.4
32         4.1         4.1
33         4.2         4.2
36         3.5         3.5
39         3.4         3.4
44         3.8         3.8
46         3.8         3.8
48         3.7         3.7
============================

# Python通过索引获取数据的部分子集，由 loc和 iloc可以实现，iloc应用较少，基于位置进行筛选的
# 取出前 5行
iris.iloc[0:5, [1,3]]

===========================
   SepalWidth  PetalWidth
0         3.5         0.2
1         3.0         0.2
2         3.2         0.2
3         3.1         0.2
4         3.6         0.2
===========================


# # R
# # 一个变量的观测筛选
# head(subset(iris, Name=='Iris-setosa'))
#
# ==============================================================
#   SepalLength SepalWidth PetalLength PetalWidth        Name
# 1         5.1        3.5         1.4        0.2 Iris-setosa
# 2         4.9        3.0         1.4        0.2 Iris-setosa
# 3         4.7        3.2         1.3        0.2 Iris-setosa
# 4         4.6        3.1         1.5        0.2 Iris-setosa
# 5         5.0        3.6         1.4        0.2 Iris-setosa
# 6         5.4        3.9         1.7        0.4 Iris-setosa
# ==============================================================
#
# # 两个变量的观测筛选
# head(subset(iris, Name=='Iris-setosa' & SepalLength>5))
#
# ==============================================================
#    SepalLength SepalWidth PetalLength PetalWidth        Name
# 1          5.1        3.5         1.4        0.2 Iris-setosa
# 6          5.4        3.9         1.7        0.4 Iris-setosa
# 11         5.4        3.7         1.5        0.2 Iris-setosa
# 15         5.8        4.0         1.2        0.2 Iris-setosa
# 16         5.7        4.4         1.5        0.4 Iris-setosa
# 17         5.4        3.9         1.3        0.4 Iris-setosa
# ==============================================================
#
# # 两个变量的观测筛选并筛选部分变量
# head(subset(iris, Name=='Iris-setosa' & SepalLength>5, select = c('SepalLength', 'SepalWidth')))
#
# ===========================
#    SepalLength SepalWidth
# 1          5.1        3.5
# 6          5.4        3.9
# 11         5.4        3.7
# 15         5.8        4.0
# 16         5.7        4.4
# 17         5.4        3.9
# ===========================



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 变量的删除
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 删除 SepalLength和 Name变量
iris.drop(['SepalLength', 'Name'], axis=1).head()

=========================================
   SepalWidth  PetalLength  PetalWidth
0         3.5          1.4         0.2
1         3.0          1.4         0.2
2         3.2          1.3         0.2
3         3.1          1.5         0.2
4         3.6          1.4         0.2
=========================================

# R
# head(subset(iris, select=-c(SepalWidth, Name)))
#
# =======================================
#   SepalLength PetalLength PetalWidth
# 1         5.1         1.4        0.2
# 2         4.9         1.4        0.2
# 3         4.7         1.3        0.2
# 4         4.6         1.5        0.2
# 5         5.0         1.4        0.2
# 6         5.4         1.7        0.4
# =======================================



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 变量重命名
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 修改变量名称

iris.rename(columns={'SepalLength':'Sepal_Length', 'SepalWidth':'Sepal_Width'}, inplace=True)
iris.head()

====================================================================
   Sepal_Length  Sepal_Width  PetalLength  PetalWidth         Name
0           5.1          3.5          1.4         0.2  Iris-setosa
1           4.9          3.0          1.4         0.2  Iris-setosa
2           4.7          3.2          1.3         0.2  Iris-setosa
3           4.6          3.1          1.5         0.2  Iris-setosa
4           5.0          3.6          1.4         0.2  Iris-setosa
====================================================================


# R
# install.packages('plyr')
#
# head(iris,2)
#
# =============================================================
#   SepalLength SepalWidth PetalLength PetalWidth        Name
# 1         5.1        3.5         1.4        0.2 Iris-setosa
# 2         4.9        3.0         1.4        0.2 Iris-setosa
# =============================================================
#
# library(plyr)
# iris_rename <- rename(iris, c('SepalLength'='Sepal.Length', 'SepalWidth'='Sepal.Width'))
#
# head(iris_rename, 2)
#
# ===============================================================
#   Sepal.Length Sepal.Width PetalLength PetalWidth        Name
# 1          5.1         3.5         1.4        0.2 Iris-setosa
# 2          4.9         3.0         1.4        0.2 Iris-setosa
# ===============================================================



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 数据类型转化
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 字符型数值转数值

data = pd.DataFrame({'id':range(4), 'age':['13','18','11','18'], 'outconme':['15.3','10.8','13.7','11.4']})
data

=====================
   id age outconme
0   0  13     15.3
1   1  18     10.8
2   2  11     13.7
3   3  18     11.4
=====================

data.dtypes

=====================
id           int64
age         object
outconme    object
dtype: object
=====================


# 字符型数值转数值--对不同的变量设置不同数据类型
data = data.astype({'outconme':'float', 'age':'int'})
data.dtypes

=====================
id            int64
age           int32
outconme    float64
dtype: object
=====================
# 通过字典的方式，对不同的变量设置不同的数据类型


# # R
# # 使用as.numeric()和as.integer()函数完成字符型数值变量的数值型变换
#
# data = data.frame(id=1:4, age=c('13','18','11','18'), outconme=c('15.3','10.8','13.7','11.4'))
# data
#
# ====================
#   id age outconme
# 1  1  13     15.3
# 2  2  18     10.8
# 3  3  11     13.7
# 4  4  18     11.4
# ====================
#
# str(data)
#
# =============================================================
# 'data.frame':	4 obs. of  3 variables:
#  $ id      : int  1 2 3 4
#  $ age     : Factor w/ 3 levels "11","13","18": 2 3 1 3
#  $ outconme: Factor w/ 4 levels "10.8","11.4",..: 4 1 3 2
#  =============================================================
#
# data$age <- as.integer(as.character(data$age))
# data$outconme <- as.numeric(as.character(data$outconme))
#
# str(data)
#
# ==========================================
# 'data.frame':	4 obs. of  3 variables:
#  $ id      : int  1 2 3 4
#  $ age     : int  13 18 11 18
#  $ outconme: num  15.3 10.8 13.7 11.4
# ==========================================



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 数据集的排序
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# 可以随意的按某些变量升序或降序排序
iris.sort_values(by = ['Sepal_Length', 'Sepal_Width'], ascending=[True,False]).head()

======================================================================
    Sepal_Length  Sepal_Width  PetalLength  PetalWidth         Name
13           4.3          3.0          1.1         0.1  Iris-setosa
42           4.4          3.2          1.3         0.2  Iris-setosa
38           4.4          3.0          1.3         0.2  Iris-setosa
8            4.4          2.9          1.4         0.2  Iris-setosa
41           4.5          2.3          1.3         0.3  Iris-setosa
======================================================================

# R
# test <- arrange(iris, SepalLength, desc(SepalWidth))
# head(test)
#
# =============================================================
#   SepalLength SepalWidth PetalLength PetalWidth        Name
# 1         4.3        3.0         1.1        0.1 Iris-setosa
# 2         4.4        3.2         1.3        0.2 Iris-setosa
# 3         4.4        3.0         1.3        0.2 Iris-setosa
# 4         4.4        2.9         1.4        0.2 Iris-setosa
# 5         4.5        2.3         1.3        0.3 Iris-setosa
# 6         4.6        3.6         1.0        0.2 Iris-setosa
# =============================================================



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 数据去重
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# 判断数据是否重复，并完成数据集的去重
data = pd.DataFrame({'name':['Liu','Li','Chen','Liu'], 'age':[28,31,27,28],'gender':['M','M','M','M']})
data

=====================
   name  age gender
0   Liu   28      M
1    Li   31      M
2  Chen   27      M
3   Liu   28      M
=====================

# 检测观测是否重复
data.duplicated()

================
0    False
1    False
2    False
3     True
dtype: bool
================

# 删除重复数据
data.drop_duplicates()

======================
   name  age gender
0   Liu   28      M
1    Li   31      M
2  Chen   27      M
======================

# 指定变量的重复性检查
data.duplicated(subset='gender')

=============
0    False
1     True
2     True
3     True
dtype: bool
=============


# # R
# data = data.frame(name=c('Liu','Li','Chen','Liu'),age=c(28,31,27,28),gender=c('M','M','M','M'))
# data
#
# ====================
#   name age gender
# 1  Liu  28      M
# 2   Li  31      M
# 3 Chen  27      M
# 4  Liu  28      M
# ====================
#
# duplicated(data)
#
# ==============================
# [1] FALSE FALSE FALSE  TRUE
# ==============================
#
# data[!duplicated(data),]
#
# ====================
#   name age gender
# 1  Liu  28      M
# 2   Li  31      M
# 3 Chen  27      M
# ====================



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 抽样
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# 通过抽样构建训练集和测试集，训练集用来模型的生成，测试集用来模型的检验
# pandas模块有一个 sample函数可以帮助我们完成抽样的任务

sample(n=None, frac=None, replace=False, weights=None, random_state=None)
n: 指定抽样的个数
frac: 指定抽样的比例
replace: 指定是否有放回的抽样，默认为无放回抽样
weights: 指定每个样本被抽中的概率，默认每个样本抽中的概率相等
random_state: 指定抽样的随机种子，默认无固定的随机种子，即每次抽样的结果都不一样

# # 抽样实例
# 训练集
train = iris.sample(frac = 0.8, random_state=1)
# 测试集
test = iris.loc[~iris.index.isin(train.index),:]

print('训练集的行、列数：', train.shape)
print('\n')
print('测试集的行、列数：', test.shape)

============================
训练集的行、列数： (120, 5)


测试集的行、列数： (30, 5)
============================


# # R
# # sample函数，参数与pandas类似
# sample(x= , size= , replace=FALSE, prob=NULL)
# x: 为抽样的对象
# size: 为抽取的样本量
# replace: 指定是否有放回的抽样，默认无放回抽样
# prob: 指定样本抽中概率，默认每个样本被抽中的概率一样
#
# # 设置抽样的随机种子
# set.seed(1)
# # 抽取数据集的行号
# index <- sample(1:nrow(iris), size=0.8*nrow(iris))
# # 根据抽出来的行号，通过抽样构建训练集和测试集
# train <- iris[index,]
# test <- iris[-index,]
# # 数据维度
# dim(train)
#
# ==============
# [1] 120   5
# ==============
#
# dim(test)
#
# ==============
# [1] 30  5
# ==============
