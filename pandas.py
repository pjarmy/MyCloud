import numpy as np; import pandas as pd


# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 数据结构介绍

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # Series的创建：

# 1、通过一位数字创建序列
arr1 = np.arange(10)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
type(arr1)

s1 = pd.Series(arr1)
s1
type(s1)

# 2、通过制度的方式创建序列
dic1 = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
type(dic1)

s2 = pd.Series(dic1)
s2
type(s2)

# 3、通过DataFrame中的某一行或某一列创建序列
# ...



# # # DataFrame的创建：

# 1、通过二维数组创建数据框
arr2 = np.array(np.arange(12)).reshape(4,3)
arr2
type(arr2)

df1 = pd.DataFrame(arr2)
df1
type(df1)

# 2、通过字典的方式创建数据框
dic2 = {'a':[1,2,3,4], 'b':[5,6,7,8], 'c':[9,10,11,12], 'd':[13,14,15,16]}
dic2
type(dic2)

df2 = pd.DataFrame(dic2)
df2
type(df2)


dic3 = {'one':{'a':1, 'b':2, 'c':3, 'd':4}, 'two':{'a':5, 'b':6, 'c':7, 'd':8}, 'three':{'a':9, 'b':10, 'c':11, 'd':12}}
dic3
type(dic3)

df3 = pd.DataFrame(dic3)
df3
type(df3)

# 3、通过数据框的方式创建数据框
df4 = df3[['one','three']]
df4
type(df4)

s3 = df3['one']
s3
type(s3)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 数据索引index

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # 1、通过索引值或索引标签获取数据：
s4 = pd.Series(np.array([1,1,2,3,5,8]))
s4
s4.index
s4.index = ['a','b','c','d','e','f']
s4

# 数据获取
s4[3]
s4['e']
s4[[1,3,5]]
s4[['a','b','d','f']]
s4[:4]
s4['c':]
s4['b':'e']


# # # 2、自动化对齐：
s5 = pd.Series(np.array([10,15,20,30,55,80]), index = ['a','b','c','d','e','f'])
s5

s6 = pd.Series(np.array([12,11,13,15,14,16]), index = ['a','c','g','b','d','f'])
s6

s5 + s6
s5 / s6



# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 利用pandas查询数据

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 































