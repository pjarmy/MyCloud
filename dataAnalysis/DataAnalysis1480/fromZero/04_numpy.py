# 数学领域的线性代数、傅里叶变换；统计学领域的统计计算、随机数生成等

# 统计里面的计算和随机数生成作讲解

# # 使用numpy构建矩阵
import numpy as np
arr1 = np.array([1,3,5,7,9])
print(arr1)

arr2 = np.array((10,20,30,40,50))
print(arr2)

arr3 = np.array([[1,2,3,4],[5,6,7,8],[3,4,5,6]])
print(arr3)

========================
[1 3 5 7 9]
[10 20 30 40 50]
[[1 2 3 4]
 [5 6 7 8]
 [3 4 5 6]]
 ========================


print(arr1.shape)
print(arr3.shape)

============
(5,)
(3, 4)
============



# # 元素的获取

print(arr3, '\n')
# 获取二维数组的某行
print(arr3[:2], '\n')
# 获取二维数组的某列
print(arr3[1,:], '\n')
# 获取二维数组的某个元素
print(arr3[2,3], '\n')

================
[[1 2 3 4]
 [5 6 7 8]
 [3 4 5 6]]

[[1 2 3 4]
 [5 6 7 8]]

[5 6 7 8]

6
================


print(arr3, '\n')
# 获取二维数组的某几行
print(arr3[[0,2], :], '\n')
# 获取二维数组的某几列
print(arr3[:,[0,1,3]], '\n')
# 获取二维数组的某几行某几列元素
print(arr3[[0,2],[2,3]], '\n')

===============
[[1 2 3 4]
 [5 6 7 8]
 [3 4 5 6]]

[[1 2 3 4]
 [3 4 5 6]]

[[1 2 4]
 [5 6 8]
 [3 4 6]]

[3 6]
===============


print(arr3, '\n')
# 取两次索引
print(arr3[[0,2],:][:,[2,3]], '\n')

# 更加坚定的方法--使用ix_函数
print(arr3[np.ix_([0,2],[2,3])])

=====================
[[1 2 3 4]
 [5 6 7 8]
 [3 4 5 6]]

[[3 4]
 [5 6]]

[[3 4]
 [5 6]]
=====================



# # 数学函数

# 取绝对值
np.abs
np.fabs
# 算数平方根
np.sqrt
# 平方
np.square
# 指数
np.exp
# 对数
np.log2
np.log10
np.log(x,base)
# 符号函数（大于0的数返回1、小于0的数返回-1、0返回0值）
np.sign
# 向上取整
np.cell
# 向下取整
np.floor
# 返回最近的整数
np.rint
# 判断是否缺失
np.isnan
# 判断是否有限
np.isfinite
# 判断是否无限
np.isinf
# 幂运算
np.power
# 余数
np.mod


# # 统计函数

# 最大值
np.max
# 浮点型的最大值
np.fmax
# 最小值
np.min
# 浮点型的最小值
np.fmin
# 求和
np.sum
# 均值
np.mean
# 标准差
np.std
# 方差
np.var
# 中位数
np.median


# # 映射函数
apply_along_axis

print(arr3, '\n')
# 对矩阵的每一行计算均值
print(np.apply_along_axis(func1d=np.mean, axis=1, arr=arr3), '\n')
# 对矩阵的每一列计算和
print(np.apply_along_axis(func1d=np.sum, axis=0, arr=arr3), '\n')

==============
[[1 2 3 4]
 [5 6 7 8]
 [3 4 5 6]]

[2.5 6.5 4.5]

[ 9 12 15 18]
==============


# # 随机数生成等
random


# # 离散分布

import numpy as np
# 设置随机种子，保证每次运行都会出现相同的随机数
np.random.seed(123)
# 二项分布

# 在概率论和统计学中，二项分布是n个独立的是/非试验中成功的次数的离散概率分布，其中每次试验的成功概率为p

r1 = np.random.binomial(n=10, p=0.2, size=10)
print(r1, '\n')

r2 = np.random.binomial(n=10, p=0.2, size=(3,5))
print(r2, '\n')

========================
[3 1 1 2 3 2 5 3 2 2]

[[1 3 2 0 2]
 [3 1 1 2 2]
 [2 3 3 2 3]]
========================

# size参数可以用来控制生成的随机数的形状，r1就是一个10个长度的一维数组；r2就是一个3×5的矩阵。


# 泊松分布

# 该分布适合于描述单位时间（或空间）内随机事件发生的次数。如某一服务设施在一定时间内到达的人数，电话交换机接到呼叫的次数，汽车站台的候客人数，机器出现的故障数。

import numpy as np
# 设置随机种子，保证每次运行都会出现相同的随机数
np.random.seed(1)
# 泊松分布
r3 = np.random.poisson(lam=6, size=10)
print(r3, '\n')

r4 = np.random.poisson(lam=(10, 50, 20), size=(5,3))
print(r4, '\n')


=========================
[2 3 7 7 4 6 5 6 2 4]

[[11 52 13]
 [12 34 22]
 [17 61 19]
 [16 55 26]
 [12 45 22]]
=========================


# # 连续分布

# 正态分布
import numpy as np
# 设置随机种子
np.random.seed(2)
# 正态分布（均值为2，标准差为3）
r5 = np.random.normal(loc=2, scale=3, size=10)
print(r5, '\n')

r6 = np.random.normal(loc=2, scale=3, size=(3,5))
print(r6, '\n')

============================================================================
[ 0.74972646  1.83119952 -4.40858829  6.92081243 -3.38030676 -0.5252421
  3.50864425 -1.73586426 -1.17385666 -0.72702284]

[[ 3.65436213  8.87662404  2.12461818 -1.35377634  3.61717496]
 [ 0.2115209   1.94260851  5.52500366 -0.24361285  2.02707575]
 [-0.63432368  1.53069749  2.76971136 -0.96633715  0.9835341 ]]
============================================================================

# 其他常用分布

import numpy as np
# 设置随机种子
np.random.seed(3)
# 自由度为2的t分布
r7 = np.random.standard_t(df=3, size=(2,3))
print(r7, '\n')
# 自由度为2和5的f分布
r8 = np.random.f(dfnum=2, dfden=5, size=(3,5))
print(r8, '\n')
# 1到10之间均匀分布，并四舍五入取整
r9 = np.round(np.random.uniform(size=(3,4), low=1, high=10), 0)
print(r9, '\n')

==============================================================
[[ 1.67789635  1.09808087 -0.37427898]
 [-0.53594414 -1.03724199 -0.38205037]]

[[1.37777325 1.07072174 1.52841252 0.30383464 2.82002052]
 [0.45387345 7.70028204 0.35583798 0.47004379 4.97319182]
 [1.20554524 0.96989918 0.33543628 2.73817049 1.4080014 ]]

[[ 4.  5.  2.  3.]
 [10.  3.  7.  7.]
 [ 8.  5.  6.  2.]]
==============================================================

# # 数据加载
>>>>>>> 18e85eb0314390a69f64a0c319e14b5f4f403606

# 数据加载
data1 = np.loadtxt(fname='E:/Documents/testfile/loadtxt.txt', delimiter=',', skiprows=1)
data2 = np.genfromtxt(fname='E:/Documents/testfile/loadtxt.txt', delimiter=',', skip_header=1, usecols=[0,2])

print(data1, '\n')
print(data2)

=========================
[[ 5.  6.  7.  8.]
 [ 9. 10. 11. 12.]
 [13. 14. 15. 16.]]

[[ 5.  7.]
 [ 9. 11.]
 [13. 15.]]
=========================

# fname：		指定外部文件的路径
# delimiter：	指定文件中数据列的分隔符
# skiprows：	指定读数时跳过的行数
# skip_header：	指定跳过首行
# usecols：		指定读取的数据列


# # 数据写出

# 通过使用 numpy模块中的 savetxt函数实现 python数据的写出，函数语法如下：

# np.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ')

# fname：指定数据写出的路径
# X：指定需要写出的数据
# fmt：指定输出数据的格式，默认科学计算法
# delimiter：指定数据列之间的分隔符，默认空格符
# newline：指定新行的标识符，默认换行
# header：指定输出数据首行值
# footer：指定输出数据的末行值
# comments：指定注释符，默认“#”