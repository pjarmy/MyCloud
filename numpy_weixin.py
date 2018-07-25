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






 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
