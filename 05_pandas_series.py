# 列表无法与一个标量进行运行（虽然乘法*不报错，但其表示重复）
ls1 = [1,3,5]
ls1 + 10

# 显示无法将列表与整形值连接，“+”运算在列表中是连接操作
================================================================================
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-20-d798d784f48d> in <module>()
      1 # 列表无法与一个标量进行运行（虽然乘法*不报错，但其表示重复）
      2 ls1 = [1,3,5]
----> 3 ls1 + 10

TypeError: can only concatenate list (not "int") to list
================================================================================


import pandas as pd
# 将列表转换为序列
series1 = pd.Series(ls1)
series1 + 10

===============
0    11
1    13
2    15
dtype: int64
===============


# 元素级的数学函数
ls1 = [1,3,5]
pow(ls1, 2)

================================================================================
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-25-f709cb4b6d67> in <module>()
      1 # 元素级的数学函数
      2 ls1 = [1,3,5]
----> 3 pow(ls1, 2)

TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
================================================================================


import pandas as pd
# 将列表转换为序列
series1 = pd.Series(ls1)
pow(series1,2)

================
0     1
1     9
2    25
dtype: int64
================


# # 序列的索引

# 位置索引
import numpy as np
import pandas as pd
np.random.seed(1)
s1 = pd.Series(np.random.randint(size=5, low=1, high=10))
print(s1, '\n')
print(s1[0], '\n')
print(s1[1:3], '\n')
print(s1[::2], '\n')

===============
0    6
1    9
2    6
3    1
4    1
dtype: int32

6

1    9
2    6
dtype: int32

0    6
2    6
4    1
dtype: int32
===============


# 倒数的方式取元素，序列就显得不是很方便了，我们推荐使用非常棒的iat方法，该方法不管应用于序列还是数据框都非常优秀，主要体现在简介而高速
print(s1.iat[-3], '\n')
print(s1[-3:], '\n')

==============
6

2    6
3    1
4    1
dtype: int32
==============


# 布尔索引
import numpy as np
import pandas as pd
np.random.seed(23)
s1 = pd.Series(np.random.randint(size=5, low=1, high=100))
print(s1)
# 取出大于等于70的值
print(s1[s1>=70])

# 取出40~50之间的值
s1[s1>=40][s1<50]

===============
0    84
1    41
2    74
3    55
4    32
dtype: int32
0    84
2    74
dtype: int32
Out[29]:
1    41
dtype: int32
===============


# R语言中一个向量的元素是否包含于另一个向量，可以使用%in%函数进行判断
# 对于一个一维数组，in1d函数实现该功能；对于一个序列，isin方法可实现该功能

# 序列元素成员关系
import numpy as np
import pandas as pd

arr1 = np.array([1,2,3,4])
arr2 = np.array([10,20,3,40])
print(np.in1d(arr1, arr2), '\n')

s1 = pd.Series(['A','B','C','D'])
s2 = pd.Series(['X','A','Y','D'])
print(s1.isin(s2))
print(np.in1d(s1,s2), '\n')

===========================
[False False  True False]

0     True
1    False
2    False
3     True
dtype: bool
[ True False False  True]
===========================


# 序列去重及水平统计
import numpy as np
import pandas as pd

np.random.seed(10)
s = np.random.randint(size=1000, low=1, high=4)
# 排重
print(pd.unique(s), '\n')
# 水平统计
print(pd.value_counts(s))

===============
[2 1 3]

3    342
2    334
1    324
dtype: int64
===============
# 借助于unique函数（与R语言一样的函数）实现序列的排重，获得不同的水平值；通过使用value_counts函数（对应于R语言的table函数）对各个水平进行计数，并按频次降序呈现


# 序列的排序（排序函数默认升序）
import numpy as np
import pandas as pd

np.random.seed(1)
s = pd.Series(np.random.normal(size=4))
# 按序列的索引排序
print(s.sort_index(ascending=False), '\n')   # 按索引降序排列
# 按序列的值排序
print(s.sort_values())    # 按序列的实际值升序排列


# # sample函数、抽样

s.sample(n=None, frac=None, replace=False, weights=None, random_stat=N)

# n:                指定抽取的样本量
# frac: 			指定抽取的样本比例
# replace: 			是否有放回抽样，默认无放回
# weights: 			指定样本中的概率，默认等概论抽样
# random_stat3: 		指定抽样的随机种子

# 从1...100中随机抽取3个幸运儿
s = pd.Series(range(1,101))
print(s.sample(n=3, random_state=2), '\n')

# 从1...5中有放回的抽取3个值
s = pd.Series(range(1,6))
print(s.sample(n=3, replace=True, random_state=2), '\n')

=================
83    84
30    31
56    57
dtype: int64

0    1
0    1
3    4
dtype: int64
=================


# 从男、女性别中不等概率抽10个样本
s = pd.Series(['男','女'])
s.sample(n=10, replace=True, weights=[0.2,0.8], random_state=3)

=================
1    女
1    女
1    女
1    女
1    女
1    女
0    男
1    女
0    男
1    女
dtype: object
=================


# # 统计运算

describe函数（类似R中的summary）

# 序列汇总
import numpy as np
import pandas as pd

np.random.seed(1234)
s = pd.Series(np.random.randint(size=100, low=10, high=30))
s.describe()

========================
count    100.000000
mean      20.360000
std        5.670266
min       10.000000
25%       15.750000
50%       21.000000
75%       25.000000
max       29.000000
========================


# count是序列中非缺失元素的个数，如何判断一个序列元素是否为缺失呢，可以用isnull函数（R中的is.na）

# 缺失值的判定

import numpy as np
import pandas as pd

s = pd.Series([1,2,np.nan,4,np.nan,6])
print(s, '\n')
print(s.isnull())

=================
0    1.0
1    2.0
2    NaN
3    4.0
4    NaN
5    6.0
dtype: float64

0    False
1    False
2     True
3    False
4     True
5    False
dtype: bool
=================


# # 常用统计函数

s.min()                # 最小值
s.quantile(q=[0,0.25,0.5,0.75,1])       # 分位数函数
s.median()             # 中位数
s.mode()               # 余数
s.mean()               # 平均值
s.mad()                # 平均绝对误差
s.max()                # 最大值
s.sum()                # 和
s.std()                # 标准差
s.var()                # 方差
s.skew()               # 偏度
s.kurtosis()           # 峰度
s.cumsum()             # 和的累计，返回序列
s.cumprod()            # 乘积的累积，返回序列
s.product()            # 序列元素乘积
s.diff()               # 序列差异（微分），返回序列
s.abs()                # 绝对值，返回序列
s.pct_change()         # 百分比变化，返回序列
s.corr(s2)             # 相关系数
s.ptp()                # 极差 R中的range函数

























