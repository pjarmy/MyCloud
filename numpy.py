import numpy as np


# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 数组的创建 
# numpy中使用  array()  函数创建数组, array的首个参数一定是一个序列，可以是元组也可以是列表。

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 



# # # 一维数组：

ls1 = range(10)
list(ls1)
type(ls1)
# range   列表类型

ls2 = np.arange(10)
list(ls2)
type(ls2)
# numpy.ndarray   
# 一维数组


arr1 = np.array((1,20,13,28,22))
arr1
type(arr1)
# numpy.ndarray
# 元组序列构成的一维数组


arr2 = np.array([1,1,2,3,5,8,13,21])
arr2
type(arr2)
# 列表序列构成的一维数组




# # # 二维数组：

arr3 = np.array(((1,1,2,3),(5,8,13,21),(34,55,89,144)))
arr3
# 元组套元组

arr4 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
arr4
# 列表套列表




# # # 特殊数组：

# 返回一维元素全为1的数组
np.ones(3)
# 返回元素全为1的3×4二维数组
np.ones([3,4])


# 返回一维元素全为0的数组
np.zeros(3)
# 返回元素全为0的3×4二维数组
np.zeros([3,4])


# 返回一维空数组
np.empty(3)
# 返回3×4二维空数组
np.empty([3,4])



# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 有关数组的属性和函数

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# # # 数组的方法：

arr3
# shape方法返回数组的行数和列数
arr3.shape
# dtype方法返回数组的数据类型
arr3.dtype
# 通过ravel的方法将数组拉直（多维数组降为一维数组）
a = arr3.ravel()
a
# 通过flatten的方法将sz拉直
b = arr3.flatten()
b

# avel方法生成的是原数组的视图，无需占有内存空间，但视图的改变会影响到原数组的变化。
# flatten方法返回的是真实值，其值的改变并不会影响原数组的更改。
# EX:
b[:3] = 0         # 通过更改 b 的值，原数组没有变化
arr3
a[:3] = 0         # a的值变化后，会导致原数组跟着变化
arr3
a
b

arr4
# 返回数组的维数
arr4.ndim
# 返回数组元素的个数
arr4.size
# 返回数组的转置结果
arr4.T

# 如果数组的数据类型为复数的话，real方法可以返回复数的实部，imag方法返回复数的虚部。



# # # 数组的函数：
arr3
arr4

np.column_stack((arr3,arr4))
np.hstack((arr3, arr4))
# 横向拼接arr3和arr4两个数组，但必须满足两个数组的行数相同。

np.vstack((arr3,arr4))
np.row_stack((arr3,arr4))
# 纵向拼接arr3和arr4两个数组，但必须满足两个数组的列数相同。



arr5 = np.array(np.arange(24))
arr5

# 通过reshape函数将一维数组设置为二维数组，且为4行6列的数组。
a = arr5.reshape(4,6)
a

# 通过resize函数会直接改变原数组的形状。
a.resize(6,4)
a

# 数组转换：tolist将数组转换为列表，astype()强制转换数组的数据类型
b = a.tolist()
b
type(b)
# list

c = a.astype(float)
c
a.dtype
dtype('int32')
c.dtype
dtype('float64')




# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 数组元素的获取

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# 通过索引和切片的方式获取数组元素，一维数组元素的获取与列表、元组的获取方式一样
arr7 = np.array(np.arange(10))
arr7

arr7[3]
arr7[:3]
arr7[3:]
arr7[-2:]
arr7[::2]

# 二维数组元素的获取
arr8 = np.array(np.arange(12)).reshape(3,4)
arr8
arr8[1]          # 返回数组的第2行
arr8[:2]         # 返回数组的前2行
arr8[[0,2]]      # 返回制定的第1行和第3行
arr8[:,0]        # 返回数组的第1列
arr8[:,-2:]      # 返回后2列
arr8[:,[0,2]]    # 返回数组的第1列和第3列
arr8[1,2]        # 返回数组中第2行第3列对应的元素


# 布尔索引，即索引值为True和False，需要注意的是布尔索引必须输数组对象。
log = np.array([True, False, False, True, True, False])
arr9 = np.array(np.arange(24)).reshape(6,4)
arr9

arr9[log]        # 返回所有为True的对应行
arr9[~log]       # 通过反选筛出所有为False的对应行

# 举一个场景，一维数组表示区域，二维数组表示观测值，如何选取目标区域的观测？
area = np.array(['A','B','A','C','A','B','D'])
area

observes = np.array(np.arange(21).reshape(7,3))
observes

observes[area == 'A']
observes[(area=='A')|(area=='D')]
observes[area == 'A'][:,[0,2]]






np.median(arr11)                      # 计算所有元素的中位数
np.median(arr11, axis = 0)            # 计算每一列的中位数
np.var(arr12)                         # 计算所有元素的方差
np.std(arr12, axis = 1)               # 计算每一行的标准差
np.sign(arr11)                        # 把矩阵变成 1,0，-1元素的矩阵
np.where(arr11 < 0, 'negtive','positive')        	# 它类似于Excel中的if函数
np.unique(arr12)                      # 计算x的唯一元素，并返回有序的结果
np.intersect1d(arr11,arr12)           # 计算x和y的公共元素，即交集
np.union1d(arr11,arr12)               # 计算x和y的并集
np.setdiff1d(arr11,arr12)             # 计算x和y的差集，即元素在x中，不在y中
np.setxor1d(arr11,arr12)              # 计算集合的对称集，即存在于一个数组中，但不同时存在于两个数组中
np.in1d(arr11,arr12)                  # 判断x的元素是否包含于y中




# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 线性代数运输

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

arr13 = np.array([[1,2,3,5],[2,4,1,6],[1,1,4,3],[2,5,4,1]])
arr13
np.linalg.det(arr13)                   # 返回方阵的行列式
np.linalg.inv(arr13)                   # 返回方阵的逆
np.trace(arr13)                        # 返回方阵的迹
np.linalg.eig(arr13)                   # 返回由特征根和特征向量组成的元组
np.linalg.qr(arr13)                    # 返回方阵的QR分解
np.linalg.svd(arr13)                   # 返回方阵的奇异值分解
np.dot(arr13,arr13)                    # 方阵的正真乘积运算

arr14 = np.array([[1,-2,1],[0,2,-8],[-4,5,9]])          # x1, x2, x3
vector = np.array([0,8,-9])                             # y
np.linalg.solve(arr14, vector)         # 求解 多远一次方程组
# array([29., 16.,  3.])


# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 随机数生成

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# 统计学中经常会讲到数据的分布特征，如正态分布、指数分布、卡方分布、二项分布、泊松分布等，下面就讲讲有关分布的随机数生成。

# # # 正太分布直方图
# pip install matplotlib

import numpy as np
# from matplotlib import *
from pylab import *                              # 用于绘图的模块

np.random.seed(1234)                             # 设置随机种子
N = 10000                                        # 随机产生的样本量
randnorm = np.random.normal(size = N)            # 生成正态随机分布
# 绘制直方图，将以上直方图频数和组距存放在counts和bins内
# counts, bins, path = matplotlib.pylab.hist(randnorm, bins = np.sqrt(N), normed = True, color = 'blue')
counts, bins, path = matplotlib.pylab.hist(randnorm, bins = int(np.sqrt(N)), density = True, color = 'blue')
sigma = 1; mu = 0
norm_dist = (1/np.sqrt(2*sigma*np.pi))*np.exp(-((bins-mu)**2)/2)
matplotlib.pylab.plot(bins,norm_dist,color = 'red')
show()


# # # 使用二项分布进行赌博
np.random.seed(1234)
binomial = np.random.binomial(9,0.5,10000)                   # 生成二项分布随机数
money = np.zeros(10000)                                      # 生成10000次赌资的列表
money[0] = 1000                                              # 首次赌资为1000元

for i in range(1,10000):
     if binomial[i] < 5:
         money[i] = money[i-1] - 8                           # 如果少于5枚正面，则输8元
     else:
         money[i] = money[i-1] + 8                           # 如果至少5枚正面，则赢8元

matplotlib.pylab.plot(np.arange(10000), money)
# plot(np.arange(10000), money)
show()


# 使用随机整数实现随机游走
np.random.seed(1234)                                       # 设定随机种子
position = 0                                               # 设置初始位置
walk = []                                                  # 创建空列表
steps = 10000                                              # 假设接下来行走10000步

for i in np.arange(steps):
     step = 1 if np.random.randint(0,2) else -1            # 每一步都是随机的
     position = position + step                            # 对每一步进行累计求和
     walk.append(position)                                 # 确定每一步所在的位置


matplotlib.pylab.plot(np.arange(10000), walk)              # 绘制随机游走图
show()


np.random.seed(1234)
step = np.where(np.random.randint(0,2,10000)>0,1,-1)
position = np.cumsum(step)
matplotlib.pylab.plot(np.arange(10000), position)
show()





































