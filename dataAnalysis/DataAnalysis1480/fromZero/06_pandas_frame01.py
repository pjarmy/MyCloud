# pandas_DataFrame01
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

# # # 数据框的构造

# # 通过列表创建数据框

# 构造数据框
import pandas as pd
pd.DataFrame([[1,2,3],[10,20,30],[100,200,300],[1,10,100]])

======================
     0    1    2
0    1    2    3
1   10   20   30
2  100  200  300
3    1   10  100
======================


import pandas as pd
pd.DataFrame([[1,2,3],[10,20,30],[100,200,300],[1,10,100]], columns=['V1','V2','V3'])

======================
    V1   V2   V3
0    1    2    3
1   10   20   30
2  100  200  300
3    1   10  100
======================
# 可以运用DataFrame函数中的columns参数给数据框的每列添加名称，如果你需要给行加上索引名称，你可以使用index参数。


# # 通过字典创建数据框

pd.DataFrame({'id':[1,2,3], 'name':['Tom','Lily','Jim'], 'age':[28,27,29]})

==================
   id  name  age
0   1   Tom   28
1   2  Lily   27
2   3   Jim   29
==================

pd.DataFrame({'id':[1,2,3], 'name':['Tom','Lily','Jim'], 'age':[28,27,29]}, columns=['id','name','age'])

==================
   id  name  age
0   1   Tom   28
1   2  Lily   27
2   3   Jim   29
==================
# R
# df <- data.frame(id=1:3, name=c('Tom','Lily','Jim'), age=c(28,27,29))
# df
# =================
  # id name age
# 1  1  Tom  28
# 2  2 Lily  27
# 3  3  Jim  29
# =================



# # 数据的读入

import pandas as pd
books = pd.read_table('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/pandas_books.txt', sep=',', header=None, usecols=[0,1,2], names=['book_typy','title','author'], encoding = 'GB2312')
books.tail()

==============================================================
  book_typy                     title author
0     excel              Excel数据处理与分析    李继兵
1     excel           Excel 2002基础与应用    赵艳霞
2     excel  Word 2000、Excel 2000使用教程    高长铎
3     excel           得心应手学Excel 2007    陈泽友
4     excel      Excel基础与应用精品教程:2007版   郭燕主编
==============================================================
# ead_table和read_csv两个函数都可以读文本文件数据，区别在于默认的sep参数不一致
# read_table默认以制表符Tab键为字段间的间隔符，而read_csv默认以逗号为字段间的间隔符


import pandas as pd
co2 = pd.read_table('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/pandas_co2.csv', sep=',')
co2.head()

=============================================
  Plant    Type   Treatment  conc  uptake
0   Qn1  Quebec  nonchilled    95    16.0
1   Qn1  Quebec  nonchilled   175    30.4
2   Qn1  Quebec  nonchilled   250    34.8
3   Qn1  Quebec  nonchilled   350    37.2
4   Qn1  Quebec  nonchilled   500    35.3
=============================================
# R
# co2 <- read.csv(file='F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/pandas_co2.csv')
# head(co2)
# ==========================================
  # Plant   Type  Treatment conc uptake
# 1   Qn1 Quebec nonchilled   95   16.0
# 2   Qn1 Quebec nonchilled  175   30.4
# 3   Qn1 Quebec nonchilled  250   34.8
# 4   Qn1 Quebec nonchilled  350   37.2
# 5   Qn1 Quebec nonchilled  500   35.3
# ==========================================


# # 电子表格的读取
!pip install xlrd
import pandas as pd
iris = pd.read_excel('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/pandas_iris.xlsx')
iris.head()

=================================================================
   Sepal.Length  Sepal.Width  Petal.Length  Petal.Width Species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
=================================================================

# R
# install.packages('readxl')
# library(readxl)
# iris <- read_excel(path='F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/pandas_iris.xlsx')
# head(iris)
# ==============================================================
# A tibble: 5 x 5
  # Sepal.Length Sepal.Width Petal.Length Petal.Width Species
         # <dbl> <chr>       <chr>        <chr>       <chr>
# 1          5.1 3.5         1.4          0.2         setosa
# 2          4.9 3.0         1.4          0.2         setosa
# 3          4.7 3.2         1.3          0.2         setosa
# 4          4.6 3.1         1.5          0.2         setosa
# 5          5   3.6         1.4          0.2         setosa
# ==============================================================


# # MYSQL数据库数据的读取

# MySQL命令
create database test;
use test;

create table user_info(
id int,
name varchar(10),
gender varchar(2),
age tinyint,
income smallint);

insert into user_info values
(1,'Tom','M',28,15000),
(2,'Lily','F',27,17000),
(3,'Lucy','F',27,15600),
(4,'Jim','M',29,20000);


import pymysql
import pandas as pd

!pip install pymysql
# 创建连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='19890201', database='test', charset='utf8')

# 读取数据
user_info = pd.read_sql('select * from user_info', conn)
user_info

==================================
   id  name gender  age  income
0   1   Tom      M   28   15000
1   2  Lily      F   27   17000
2   3  Lucy      F   27   15600
3   4   Jim      M   29   20000
==================================

# R
# install.packages('DBI')
# install.packages('RMySQL')
# library(RMySQL)
# 创建连接
# conn <- dbConnect(drv = MySQL(), host='localhost', port=3306, user='root', password='19890201', dbname='test')
# user_info <- dbGetQuery(conn, 'select * from user_info')
# user_info

# ==============================
  # id name gender age income
# 1  1  Tom      M  28  15000
# 2  2 Lily      F  27  17000
# 3  3 Lucy      F  27  15600
# 4  4  Jim      M  29  20000
# ==============================


# # 数据的概览信息

# 数据量大小情况
co2.shape
(5, 5)

# 变量的列的名称
co2.columns

============================================================================
Index(['Plant', 'Type', 'Treatment', 'conc', 'uptake'], dtype='object')
============================================================================

# shape属性和columns属性返回数据集的行列数及变量名


# 数值型变量的概览信息
co2.describe(include=['number'])

=============================
            conc    uptake
count    5.00000   5.00000
mean   274.00000  30.74000
std    157.53571   8.60802
min     95.00000  16.00000
25%    175.00000  30.40000
50%    250.00000  34.80000
75%    350.00000  35.30000
max    500.00000  37.20000
=============================


# 离散型变量的概览信息

co2.describe(include=['object'])

===================================
       Plant    Type   Treatment
count      5       5           5
unique     1       1           1
top      Qn1  Quebec  nonchilled
freq       5       5           5
===================================
# describe属性可以对数值型变量（include=['number']）和离散型变量（include=['object']）进行描述性统计；

co2.info

==============================================================================
<bound method DataFrame.info of   Plant    Type   Treatment  conc  uptake
0   Qn1  Quebec  nonchilled    95    16.0
1   Qn1  Quebec  nonchilled   175    30.4
2   Qn1  Quebec  nonchilled   250    34.8
3   Qn1  Quebec  nonchilled   350    37.2
4   Qn1  Quebec  nonchilled   500    35.3>
==============================================================================

# R
# dim(co2)
# ==========
# [1] 5 5
# ==========


# names(co2)

# ================================================================
# [1] "Plant"     "Type"      "Treatment" "conc"      "uptake"
# ----------------------------------------------------------------
# [1] "Plant"     "Type"      "Treatment" "conc"
# [5] "uptake"
# ================================================================


# summary(co2)
# # summary函数进行统计描述；
# ================================================================
# Plant       Type        Treatment      conc         uptake
 # Qn1:5   Quebec:5   nonchilled:5   Min.   : 95   Min.   :16.00
                                   # 1st Qu.:175   1st Qu.:30.40
                                   # Median :250   Median :34.80
                                   # Mean   :274   Mean   :30.74
                                   # 3rd Qu.:350   3rd Qu.:35.30
                                   # Max.   :500   Max.   :37.20
# ================================================================


# str(co2)
# # str函数对数据集的变量类型进行描述。
# ================================================================
# 'data.frame':	5 obs. of  5 variables:
 # $ Plant    : Factor w/ 1 level "Qn1": 1 1 1 1 1
 # $ Type     : Factor w/ 1 level "Quebec": 1 1 1 1 1
 # $ Treatment: Factor w/ 1 level "nonchilled": 1 1 1 1 1
 # $ conc     : int  95 175 250 350 500
 # $ uptake   : num  16 30.4 34.8 37.2 35.3
# ================================================================
