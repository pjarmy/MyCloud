Python 

# 时间转换
import datetime
dt = '2018/07/19 16:09:19'
d = '2018-07-09'

str2datetime = datetime.datetime.strptime(dt, '%Y/%m/%d %H:%M:%S')
str2date1 = datetime.datetime.strptime(d, '%Y-%m-%d')
str2date2 = datetime.datetime.strptime(d, '%Y-%m-%d').date()

In [14]: print(str2datetime)
2018-07-19 16:09:19

In [15]: print(str2date1)
2018-07-09 00:00:00

In [16]: print(str2date2)
2018-07-09


# 列表的增删改查

# 创建列表
ls = [1,2,3,'a','b','c','2018-07-20 09:33:35']
ls

# 列表：是一个可变型的序列，之所以说可变，是因为可以对列表数据类型可以进行增、删、改的操作，而不可变对象则没有这三种操作。

print(ls[0])                    # 0 表示取第一个元素
print(ls[0:2])                  # 切片方式取第一和第二个元素
print(ls[:4])                   # 切片方式取前四个元素
print(ls[3:])                   # 切片方式从第四个元素开始渠道后面的所有的元素
print(ls[-3])                   # 符索引取倒数第三个元素
print(ls[-3:])                  # 切片方式从第倒数第三个元素开始取到后面的所有元素
print(ls[-2:-5:-1])             # 切片方式到这顺序取元素
print(ls[::2])                  # 按步长为2的切片方式取元素

=========================================================
1
[1, 2]
[1, 2, 3, 'a']
['a', 'b', 'c', '2018-07-20 09:33:35']
b
['b', 'c', '2018-07-20 09:33:35']
['c', 'b', 'a']
[1, 3, 'b', '2018-07-20 09:33:35']
==========================================================


# 增
ls.append('sim')                 # 在末尾插入一个元素
print(ls)
ls.extend(['xiaoxu',25])         # 在末尾插入多个元素
print(ls)
ls.insert(-5,'Mountain')         # 在指定位置插入元素
print(ls)

==============================================================================================
[1, 2, 3, 'a', 'b', 'c', '2018-07-20 09:33:35', 'sim']
[1, 2, 3, 'a', 'b', 'c', '2018-07-20 09:33:35', 'sim', 'xiaoxu', 25]
[1, 2, 3, 'a', 'b', 'Mountain', 'c', '2018-07-20 09:33:35', 'sim', 'xiaoxu', 25]
==============================================================================================

# append方法每次只能在末尾填入一个元素；
# extend方法每次在末尾插入多个元；
# insert方法可在指定的位置插入一个元素；



# 删
ls.pop()                         # 删除末尾一个元素
print(ls)
ls.pop(-2)                       # 删除指定位置的一个元素
print(ls)
ls.remove('Mountain')            # 删除指定的元素值
print(ls)
ls2 = ls.copy()                  # 复制一个对象（非视图）
print(ls2)
ls2.clear()                      # 情况列表元素，但该列表对象仍然存在，只不过为空
print(ls2)
del ls2                          # 删除整个列表，使该对象不存在
print(ls2)

========================================================================================
[1, 2, 3, 'a', 'b', 'Mountain', 'c', '2018-07-20 09:33:35', 'sim', 'xiaoxu']
[1, 2, 3, 'a', 'b', 'Mountain', 'c', '2018-07-20 09:33:35', 'xiaoxu']
[1, 2, 3, 'a', 'b', 'c', '2018-07-20 09:33:35', 'xiaoxu']
[1, 2, 3, 'a', 'b', 'c', '2018-07-20 09:33:35', 'xiaoxu']
[]
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-10-cee399f7413a> in <module>()
     10 print(ls2)
     11 del ls2                          # 删除整个列表，使该对象不存在
---> 12 print(ls2)

NameError: name 'ls2' is not defined
========================================================================================

# pop方法在不指定参数时默认删除末尾元素，也可以指定删除某个位置的元素；
# remove方法删除指定的元素值；
# clear方法清空列表元素；
# del函数删除列表对象；



# 改
print(ls)
ls[2] = 33                         # update "3" to "33"
print(ls)
ls[3:6] = ['d','e','f']
print(ls)

===================================================================
[1, 2, 3, 'a', 'b', 'c', '2018-07-20 09:33:35', 'xiaoxu']
[1, 2, 33, 'a', 'b', 'c', '2018-07-20 09:33:35', 'xiaoxu']
[1, 2, 33, 'd', 'e', 'f', '2018-07-20 09:33:35', 'xiaoxu']
===================================================================


# 其他列表方法
ls3 = ['a','g','e','a','c','r','f','e']
ls4 = ls3.copy()                    # 复制
print(ls4)
print(ls3.count('a'))               # 计数 "a"元素出现的次数
print(ls3.index('e'))               # 返回首次出现 "e"元素的位置
ls3.reverse()                       # 颠倒元素
print(ls3)
ls3.sort()                          # 默认升序排序
print(ls3)
ls3.sort(reverse = True)            # 降序排序
print(ls3)

====================================================
['a', 'g', 'e', 'a', 'c', 'r', 'f', 'e']
2
2
['e', 'f', 'r', 'c', 'a', 'e', 'g', 'a']
['a', 'a', 'c', 'e', 'e', 'f', 'g', 'r']
['r', 'g', 'f', 'e', 'e', 'c', 'a', 'a']
====================================================

# copy方法复制一个物理对象，而非视图对象；
# count方法计数；
# index方法返回索引位置；
# reverse方法实现元素颠倒；
# sort方法排序；



# 创建一个元组
t = (1,2,3,'a','cb','lsx')
print(t)

==============================
(1, 2, 3, 'a', 'cb', 'lsx')
==============================

# 元组是不可变的序列，故其没有增、删、改的权限。只能进行查询（索引和切片）和一些简单的其他方法

# 查
In [27]: t[-1::-1]
Out[27]: ('lsx', 'cb', 'a', 3, 2, 1)


# 其他元组方法
print(t.count('a'))
print(t.index('lsx'))
import copy
t2 = copy.copy(t)
t2

# 由于元组没有copy方法，但如果你就是想复制一个物理对象给新的变量，可以考虑使用copy模块的copy方法。

==================================================
1
5
Out[28]: (1, 2, 3, 'a', 'cb', 'lsx')
==================================================



# 字典

# 字典的创建是通过花括号{}或dict函数来构造键-值对，而不是上面的中括号[]和圆括号()方法构建了

dict1 = {'id':[1,2,3,4],'name':['a','b','c','d'],'age':[20,23,25,22]}
dict2 = dict(id=list(range(1,5)), name=['lsx','xx','local','host'], gender=['f','m','m','f'])
dict3 = {'name':'lsx','score':{'shuxue':88,'yuwen':79,'yingyu':82}}
print(dict1)
print(dict2)
print(dict3)

=====================================================================================================
{'id': [1, 2, 3, 4], 'name': ['a', 'b', 'c', 'd'], 'age': [20, 23, 25, 22]}
{'id': [1, 2, 3, 4], 'name': ['lsx', 'xx', 'local', 'host'], 'gender': ['f', 'm', 'm', 'f']}
{'name': 'lsx', 'score': {'shuxue': 88, 'yuwen': 79, 'yingyu': 82}}
=====================================================================================================

# 第一个字典通过花括号构建；
# 第二个字典通过dict函数构建；
# 第三个构造了一个嵌套的字典；


# 由于字典也是一个可变对象，故其也有增、删、改的操作

# 查

print(dict1['id'])                   # 通过自低昂的键获取对应的值
print(dict1.get('name'))             # 等同于括号的索引方式，但字典中没有name键时不会报错
print(dict1.setdefault('age'))       # 等于 get 方法

print(dict1.setdefault('age1'))      # 而且如果字典中没有 age1键时会新增该键
print(dict1)
print(dict1.setdefault('age2',[0,0,0,0,]))       # 还可以为这个新键赋上对应的值
print(dict1)

======================================================================================================================
[1, 2, 3, 4]
['a', 'b', 'c', 'd']
[20, 23, 25, 22]
None
{'id': [1, 2, 3, 4], 'name': ['a', 'b', 'c', 'd'], 'age': [20, 23, 25, 22], 'age1': None}
[0, 0, 0, 0]
{'id': [1, 2, 3, 4], 'name': ['a', 'b', 'c', 'd'], 'age': [20, 23, 25, 22], 'age1': None, 'age2': [0, 0, 0, 0]}
======================================================================================================================

# 所以，setdefault方法既可以实现查的功能，又可以完成添加键值对的功能。


# 增

print(dict2)
dict2['income'] = [100,200,300,400]
print(dict2)
dict2.setdefault('age2',[0,0,0,0])
print(dict2)
dict2.update({'weight':[10,20,30,40]})
print(dict2)

====================================================================================================================================================================================
{'id': [1, 2, 3, 4], 'name': ['lsx', 'xx', 'local', 'host'], 'gender': ['f', 'm', 'm', 'f']}
{'id': [1, 2, 3, 4], 'name': ['lsx', 'xx', 'local', 'host'], 'gender': ['f', 'm', 'm', 'f'], 'income': [100, 200, 300, 400]}
{'id': [1, 2, 3, 4], 'name': ['lsx', 'xx', 'local', 'host'], 'gender': ['f', 'm', 'm', 'f'], 'income': [100, 200, 300, 400], 'age2': [0, 0, 0, 0]}
{'id': [1, 2, 3, 4], 'name': ['lsx', 'xx', 'local', 'host'], 'gender': ['f', 'm', 'm', 'f'], 'income': [100, 200, 300, 400], 'age2': [0, 0, 0, 0], 'weight': [10, 20, 30, 40]}
====================================================================================================================================================================================

# 第一个红框通过索引的方式增加键值对；
# 第二个红框通过setdefault方法增加键值对；
# 第三个红框通过update方法增加键值对；


# 删
dict2.pop('age2')                                # pop方法不像 list中的用法，必须指定键
print(dict2)
dict2.popitem()                                  # 删除末尾的一个键值对
print(dict2)

================================================================================================================================================================
{'id': [1, 2, 3, 4], 'name': ['lsx', 'xx', 'local', 'host'], 'gender': ['f', 'm', 'm', 'f'], 'income': [100, 200, 300, 400], 'weight': [10, 20, 30, 40]}
{'id': [1, 2, 3, 4], 'name': ['lsx', 'xx', 'local', 'host'], 'gender': ['f', 'm', 'm', 'f'], 'income': [100, 200, 300, 400]}
================================================================================================================================================================

# pop方法对指定的键进行删除；
# popitem方法每次删除末尾的一个键值对；


# 改

print(dict3)
dict3['name'] = 'Sim'
print(dict3)
dict3.update({'score': {'shuxue':88,'yuwen':82,'yingyu':79,'huaxue':90}})
print(dict3)

======================================================================================
{'name': 'lsx', 'score': {'shuxue': 88, 'yuwen': 79, 'yingyu': 82}}
{'name': 'Sim', 'score': {'shuxue': 88, 'yuwen': 79, 'yingyu': 82}}
{'name': 'Sim', 'score': {'shuxue': 88, 'yuwen': 82, 'yingyu': 79, 'huaxue': 90}}
======================================================================================

# 字典中更新键对应的值，既可以使用索引的方式，也可以使用update方法，但update方法中的参数一定是一个字典。如果该字典的键在dict3中存在，则操作改的动作，否则完成增加键值对的使命。


# 其他字典方法

print(list(dict3.items()))                    # 返回字典中的所有键值对
print(list(dict3.keys()))                     # 返回字典中的所有键
print(list(dict3.values()))                   # 返回字典中的所有值
dict4 = dict3.copy()                            # 复制字典
print(dict4)

===================================================================================================
[('name', 'Sim'), ('score', {'shuxue': 88, 'yuwen': 82, 'yingyu': 79, 'huaxue': 90})]
['name', 'score']
['Sim', {'shuxue': 88, 'yuwen': 82, 'yingyu': 79, 'huaxue': 90}]
{'name': 'Sim', 'score': {'shuxue': 88, 'yuwen': 82, 'yingyu': 79, 'huaxue': 90}}
===================================================================================================

# 这里需要注意的是，必须使用list函数套在items、keys、values等方法外面，否则不会产生列表结果，而是一个迭代器。



# # # 运算符

# 数值运算
# +、-、×、÷
# %        求余数
# //
# **

print(12+8)
print(33-2)
print(12*3)
print(15/4)
print(23/2)
print(23//2)
print(-23//2)

=======================
20
31
36
3.75
11.5
11
-12
=======================


# 比较运算
>、>=、<、<=
==        判断两个对象是否相等
!=        判断两个对象是否不相等


# 逻辑运算
or 或 and 且 not 非



# # # 数值函数

# python自带的数值函数
abs             # 绝对值
divmod          # 返回除法的整数和余数
round           # 四舍五入
pow             # 幂指数运算

print(abs(-3.8))
print(divmod(17,5))
print(round(17/5.3))
print(round(-4.8,0))
print(pow(2,3))

=============================
3.8
(3, 2)
3
-5.0
8
=============================


# math模块
math.pi
math.e
math.cell(x)                        # 向上取整
math.floor(x)                       # 向下取整
math.modf(expression)               # 商的小数部分与整数部分
math.log2(x)                        # 以2为底的对数
math.log10(x)                       # 以10为底的对数
math.log(x)                         # 以e为底的对数
math.log(x,base)                    # 以base为底的对数
math.exp()                          # 指数
math.sqrt()                         # 算术平方根
math.factorial()                    # 阶乘
math.fmod()                         # 返回浮点型余数



# # # 字符串处理

# 字符串索引与切片(与上一期列表、元组类似)
s1 = 'String Function'
print(s1[:6])
print(s1[-8:])

=============
String
Function
=============

# 字符串拼接（字符串的加法与join方法）
s1 = '出生年月：'
s2 = '1989'
s3 = '0717'
print(s1 + s2 + s3)

=======================
出生年月：19890717
=======================


# 加入分隔符
print(' '.join(['Python','User','to','Programe:']))
print('-'.join(['0511','87218888']))

===============================
Python User to Programe:
0511-87218888
===============================


# 字符串重复（字符串的乘法）
print('*'*40)
print('Hello, everyone. My name is Sim!')
print('*'*40)

****************************************
Hello, everyone. My name is Sim!
****************************************


# # # 字符串中的正则表达式

# 正则表达式含义

.             # 点可以代表一切字符
\             # 起转义作用
[...]         # 指代方括号中的任意字符
\d            # 指代数字0-9
\D            # 指代非数字
\s            # 指代一切空格，包括tab制表符、空格、换行等
\S            # 指代非空格
\w            # 指代大小字母、数字和下划线
\W            # 指代非大小写字母、数字和下滑线
*             # 匹配前面字符 >= 0 次
+             # 匹配前面字符 1次及以上
?             # 匹配前面字符 0 次或 1 次或
{m}           # 匹配 m次
{m,n}         # 匹配 m到 n次
{m,}          # 至少匹配m次


# # # 结合 re模块完成字符串的匹配

# # 找

# re.findall(pattern, string, flags=0)
# pattern --> 正则表达式
# string  --> 需要处理的字符串
# flags   --> 说明匹配模式，如是否大小写re.l



# 查找冒号前后的对象
import re
s1 = '''name:sim, Gender:f,
age:27, address:JianSu
Edu:yjs
'''

# 通过正则表达式将冒号前面的对象和冒号后面的对象取处理
keys = re.findall(r'([a-z]+):',s1,re.I)
values = re.findall('\w:(\w+)',s1)
# 打印
print(keys, values)

# 将键-值匹配并入字典
mydict = {}
for i in list(range(0, len(keys))):
	mydict[keys[i]] = values[i]
print(mydict)


# 查找所有含o字母的单词
s2 = 'oh, mygard. Python is an easy language, do you like it?'

rule = re.compile(r'\w*o\w*')
print(re.findall(rule, s2))

# 查出所有以 p开头的单词
s3 = 'good morning Pairs, this picture is good!'
# 不分大小写
print(re.findall('p\w+', s3, re.I))

=======================================
['oh', 'Python', 'do', 'you']
['Pairs', 'picture']
=======================================


# # 切

# re.split(pattern, string, maxsplit=0, flags=0)
# pattern   -->   正则表达式
# string    -->   需要处理的字符串
# maxsplit  -->   最大匹配次数。 0表示匹配所有次

s = 'sim@1633.com work-da intrest:pingpang'
print(re.split('[@\-:\s+]', s))

============================================================
['sim', '1633.com', 'work', 'da', 'intrest', 'pingpang']
============================================================


# # 替

sub(pattern, repl, string, count=0, flags=0)
pattern    -->     正则表达式
repl       -->     新的替换内容
string     -->     需要处理的字符串
count      -->     替换次数。0表示匹配替换所有次
flags      -->     匹配模式

# 将 1.51、1.5L、1.5t、1.5T替换为 1.5L
s = '1.5ldfn1.5LdLad1.5tsdf1.5Tadfg1.5sd'

print(re.sub('1.5[lLtT]', '1.5L', s))

=========================================
1.5Ldfn1.5LdLad1.5Lsdf1.5Ladfg1.5sd
=========================================
