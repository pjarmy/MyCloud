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





 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
