# matplotlib01

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 简单垂直条形图
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 案例一：直辖市GDP水平
# 北京、上海、天津、重庆  12406.8亿、13908.57亿、

# 导入绘图模块
import matplotlib.pyplot as plt
# 构造数据
GDP = [12406.8,13908.57,9386.87,9143.64]

# 中文乱码的处理  KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘图
plt.bar(range(4), GDP, align = 'center', color = 'steelblue', alpha = 0.8)
# align: 标签水平居中、alpha: 透明度、color: 颜色
# 添加轴标签，y轴
plt.ylabel('GDP')
# plt.xlabel('城市')
# 添加标题
plt.title('四个直辖市 GDP 大比拼')
# 添加刻度标签
plt.xticks(range(4), ['北京市','上海市','天津市','重庆市'])
# 设置 Y 轴范围
plt.ylim([5000,15000])

# 为每个条形图添加数值标签
for x,y in enumerate(GDP):
    plt.text(x,y+100, '%s' %round(y,1), ha='center')
# 显示图形
plt.show()



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 简单水平条形图
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 案例二：同一本书不同平台最低价比较
# 《python数据分析实战》在亚马逊、当当网、中国图书网、京东和天猫的最低价格分别为39.5、39.9、45.4、38.9、33.34

# 导入绘图模块
import matplotlib.pyplot as plt
# 构建数据
price = [39.5,39.9,45.4,38.9,33.34]

# 中文乱码的处理  KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘图
plt.barh(range(5), price, align='center', color='steelblue', alpha=0.8)
# 添加轴标签，x轴
plt.xlabel('价格')
# 添加标题
plt.title('不同平台书的最低价比较')
# 添加刻度标签
plt.yticks(range(5), ['亚马逊','当当网','中国图书网','京东','天猫'])
# 设置 X 轴刻度范围
plt.xlim([20,47])

# 为每个条形图添加数值标签
for x,y in enumerate(price):
    plt.text(y+0.1, x, '%s' %y, va='center')
# va：center 垂直居中， ha：center 水平居中
# 显示图形
plt.show()



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 水平较差条形图
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 以上水平、垂直条形图是基于一种离散变量的情况
# 对应两张离散变量。我们可以使用水平交错条形图和堆叠条形图

# 案例三：胡润财富榜：亿万资产超高净值家庭数

# 2016 vs 2017 City Top5

# 导入绘图模块
import matplotlib.pyplot as plt
import numpy as np
# 构建数据
Y2016 = [15600,12700,11300,4270,3620]
Y2017 = [17400,14800,12000,5200,4020]
labels = ['北京','上海','香港','深圳','广州']
bar_width = 0.45

# 中文乱码的处理  KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘图
plt.bar(np.arange(5), Y2016, label='2016', color='steelblue', alpha=0.8, width=bar_width)
plt.bar(np.arange(5)+bar_width+0.02, Y2017, label='2017', color='indianred', alpha=0.8, width=bar_width)
# 添加轴标签
plt.xlabel('Top5城市')
plt.ylabel('家庭数量')
# 添加标题
plt.title('亿万财富家庭数Top5城市分布')
# 添加刻度标签
plt.xticks(np.arange(5)+bar_width, labels)
# 设置 Y 轴刻度范围
plt.ylim([2500,19000])

# 为每个条形图添加数值标签
for x2016,y2016 in enumerate(Y2016):
    plt.text(x2016,y2016+100, '%s' %y2016)
for x2017,y2017 in enumerate(Y2017):
    plt.text(x2017+bar_width+0.01,y2017+100, '%s' %y2017)

# # 显示图例
# plt.legend()
# 显示图形
plt.show()



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 垂直堆叠条形图
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 导入模块
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 导入数据
data = pd.read_excel()





























1
