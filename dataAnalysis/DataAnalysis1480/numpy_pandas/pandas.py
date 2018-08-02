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


# # # 缺少student.csv
# student = pd.io.parsers.read_csv('C:\\Users\\admin\\Desktop\\student.csv')
student = pd.io.parsers.read_csv('D:/python3.7/TestData/student.csv')
student.head()
student.tail()

student.ix[[0,2,4,5,7]]
student[['Name','Height','Weight']].head()
student.ix[:,['Name','Height','Weight']].head()
student.ix[[0,2,4,5,7],['Name','Height','Weight']].head()
student[student['Sex']=='F']
student[(student['Sex']=='F') & (student['Age']>12)]
student[(student['Sex']=='F') & (student['Age']>12)][['Name','Height','Weight']]
 






# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 统计分析

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

np.random.seed(1234)
d1 = pd.Series(2*np.random.normal(size = 100) +3 )
d2 = np.random.f(2,4,size = 100)
d3 = np.random.randint(1100,size = 100)

d1.count()                         # 非空元素计算
d1.min()                           # 最小值
d1.max()                           # 最大值
d1.idxmin()                        # 最小值的位置，类似于 R中的which.min函数
d1.idxmax()                        # 最大值的位置，类似于 R中的which.max函数
d1.quantile(0.1)                   # 10%分位数
d1.sum()                           # 求和
d1.mean()                          # 均值
d1.median()                        # 中位数
d1.mode()                          # 众数
d1.var()                           # 方差
d1.std()                           # 标准差
d1.mad()                           # 平均绝对值
d1.skew()                          # 偏度
d1.kurt()                          # 峰度
d1.describe()                      # 一次性输出多个描述性统计指标(序列、数据框)


# 汇总：
def stats(x):
    return pd.Series([x.count(), x.min(), x.idxmin(),
		x.quantile(.25), x.median(), x.quantile(.75),x.mean(),
		x.max(), x.idxmax(), x.mad(), x.var(),
		x.std(), x.skew(), x.kurt()],
		index = ['Count','Min','Which_Min','Q1','Median','Q3','Mean','Max','Which_Max','Mad','Var','Std','Skew','Kurt'])

stats(d1)

df = pd.DataFrame(np.array([d1,d2,d3]).T, columns=['x1','x2','x3'])


# # # 离散型数据：
student['Sex'].describe()


df.corr()                           # 连续变量的相关系数
df.corr('spearman')                 # 关于相关系数的计算可以调用pearson方法或kendell方法或spearman方法，默认使用pearson方法
df.cov()                            # 数值型数据的协方差矩阵


df.corrwith(df['x1'])               # 只想关注某一个变量与其余变量的相关系数





# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 类似于SQL的操作

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # 增：添加新行或增加新列：
dic = {'Name':['LiuShunxiang','Zhangshan'],
	'Sex':['M','F'],'Age':[27,23],
	'Height':[165.7,167.2],'Weight':[61,63]
}

student2 = pd.DataFrame(dic)
student2

student3 = pd.concat([student,student2])              # 增加新行
student3


pd.DataFrame(student2, columns=['Age','Height','Name','Sex','Weight','Score'])          # 增加新列


# # # 删：删除表、观测行或变量：
del student2                       # 删除数据框 student2，通过 del可以删除 Python的所有对象

student2

student.drop [0,1,3,6]             # 删除第 1，2，4，7 行数据

student[student['Age']>=14]        # 根据布尔索引删除行数据

# 删除指定的列：
student2.drop(['Height','Weight'], axis=1).head()
student2


# # # 改：修改原始记录的值：
# student2.ix[student2['Name']=='LiuShunxiang', 'Height'] = 170
student2.loc[student2['Name']=='LiuShunxiang', 'Height'] = 170



# # # 查：
# 略



# # # 聚合：
student.groupby('Sex').mean()
student.drop('Age', axis=1).groupby('Sex').mean()
student.groupby(['Age','Sex']).mean()
student.drop('Age', axis=1).groupby('Sex').agg(np.mean, np.median)


# # # 排序：
series = pd.Series(np.array(np.random.randint(1,20,10)))
series.sort_values()                                # 按值排序，order被弃用
series.sort_values(ascending=False)                 # 降序

student.sort_values(by = ['Sex','Age'])


# # # 多表连接：
dic2 = {'Name':['Alfred','Alice','Barbara','Zhangshan','Carol','Henry','Jeffrey','Judy','Philip','Robert','William'],
	'Score':[88,76,89,62,67,79,90,92,86,73,77]
}
score = pd.DataFrame(dic2)
score

stu_scort = pd.merge(student2, score,on='Name')
stu_scort

stu_scort2 = pd.merge(student2, score,on='Name',how='left')
stu_scort2

stu_scort3 = pd.merge(student2, score,on='Name',how='right')
stu_scort3




# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 缺失值处理

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# # # 删除法  dropna([how = '[all...]'])：

s = stu_scort2['Score']
s

sum(pd.isnull(s))             # 检测有多少缺失值
s.dropna()                    # 直接删除缺失值

df = pd.DataFrame([[1,1,2],[3,5,np.nan],[13,21,34],[55,np.nan,10],
	[np.nan,np.nan,np.nan],[np.nan,1,2]],
	columns=['x1','x2','x3']
)

df
df.dropna()
df.dropna(how='all')


# # # 替补法 fillna([method='[ffill,bfill...]'], [axis=1])：

df.fillna(0)                  # 用 0 填补
df.fillna(method='ffill')     # 用前一个观测值填充
df.fillna(method='bfill')     # 用后一个观测值填充


# # # 插补法  fillna({col1:'', col2:'', ...})：

df.fillna({'x1':1, 'x2':2, 'x3':3})         # 使用常量填充不同的列

# 用均值或中位数填充各自的列
x1_median = df['x1'].median()
x2_mean = df['x2'].mean()
x3_mean = df['x3'].mean()

df.fillna({'x1':x1_median, 'x2':x2_mean, 'x3':x3_mean})




# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 数据透视表

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 对一个分组变量（Sex），一个数值变量（Height）作统计汇总
pd.pivot_table(student2, values = ['Height'], columns = ['Sex'])

# 对一个分组变量（Sex），两个数值变量（Height,Weight）作统计汇总
pd.pivot_table(student2, values = ['Height','Weight'], columns = ['Sex'])

# 对两个分组变量（Sex，Age)，两个数值变量（Height,Weight）作统计汇总
pd.pivot_table(student2, values = ['Height','Weight'], columns = ['Sex','Age'])

# 非堆叠操作，连表形式
pd.pivot_table(student2, values = ['Height','Weight'], columns = ['Sex','Age']).unstack()

# 使用多个聚合函数
pd.pivot_table(student2, values = ['Height','Weight'], columns = ['Sex'], aggfunc=[np.mean,np.median,np.std])



# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 多层索引的使用

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

np.random.seed(1234)
# 多层次索引的序列:
data = pd.Series(np.random.randint(1,20,12),
	index = [['a','a','a','b','b','b','c','c','c','d','d','d'],
	[1,2,3,1,2,3,1,2,3,1,2,3]]
)

data
data.unstack()                          # To数据框

data['a']                               # 返回外层索引为 a的所有数据
data[['a','d']]                         # 返回外层索引为 a和 d的所有数据
data[:,1]                               # 返回内层所有为 1的所有数据



np.random.seed(1234)
# 高维数据框：
df = pd.DataFrame(np.random.randint(10,50,20).reshape(5,4),
	index = [['A','A','A','B','B'], [1,2,3,1,2]],
	columns = [['X','X','X','Y'], ['x1','x2','x3','y']]
)

df

df['X']
# df.ix[['A'],:]
df.loc[['A'],:]

# # 在数据框中使用多层索引，可以将整个数据集控制在二维表结构中

pd.pivot_table(student2, index = ['Sex','Age'])









