# matplotlib_BarChart
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

# 百度百科
# 条形图（bar chart） 是用宽度相同的条形的高度或长短来表示数据多少的图形。条形图可以横置或纵置，纵置时也称为柱形图（column chart）。此外，条形图有简单条形图、复式条形 图等形式
# 区分 直方图 直方图有范围

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 简单垂直条形图
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 案例一：直辖市GDP水平
# 北京、上海、天津、重庆  12406.8亿、13908.57亿、9386.87亿、9143.64亿

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
plt.ylabel('GDP(亿)')
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



# R
# 条形图表示矩形条中的数据，条的长度与变量的值成比例。 R语言使用函数barplot()创建条形图。 R语言可以在条形图中绘制垂直和水平条。 在条形图中，每个条可以给予不同的颜色。
************************************************************
# R语言 创建条形图的基本语法
barplot(H, xlab, ylab, main, names.arg, col)
    H           是包含在条形图中使用的数值的向量或矩阵
    xlab        是 x轴的标签
    ylab        是 y轴的标签
    main        是条形图的标题
    names.arg   是在每个条下出现的名称的向量
    col         用于向途中的条形提供颜色
    xpd         逻辑值，设置柱子是否可以超出区域 TRUE/FALSE
************************************************************

# Create data for the graph.
GDP <- c(12406.8, 13908.57, 9386.87, 9143.64)
Municipalities <- c('北京市','上海市','天津市','重庆市')
# Give the chart file a name. 保存图片
png(file = "F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/Image/Municipalities_GDP.png")
# Plot the bar chart
barplot(GDP, names.arg = Municipalities, main = "四个直辖市 GDP 大比拼", ylab = 'GDP', ylim = c(5000,15000), col = 'steelblue', xpd = FALSE)
# barplot(GDP, names.arg = Municipalities, main = "Competition of Four Municipalities GDP", xlab = 'Municipalities', ylab = 'GDP', col = 'steelblue')
dev.off()



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
    plt.text(x2016,y2016+100, '%s' %y2016, ha = 'center')
for x2017,y2017 in enumerate(Y2017):
    plt.text(x2017+bar_width+0.01,y2017+100, '%s' %y2017, ha = 'center')

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
data = pd.read_excel('E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/matplotlib_货运.xlsx')

# 中文乱码的处理  KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘图
plt.bar(np.arange(8), data.loc[0,:][1:], color = 'red', alpha = 0.8, label = '铁路', align = 'center')
plt.bar(np.arange(8), data.loc[1,:][1:],  bottom = data.loc[0,:][1:], color = 'green', alpha = 0.8, label = '公路', align = 'center')
plt.bar(np.arange(8), data.loc[2,:][1:],  bottom = data.loc[0,:][1:]+data.loc[1,:][1:], color = 'm', alpha = 0.8, label = '水运', align = 'center')
plt.bar(np.arange(8), data.loc[3,:][1:],  bottom = data.loc[0,:][1:]+data.loc[1,:][1:]+data.loc[2,:][1:], color = 'black', alpha = 0.8, label = '民航', align = 'center')
# 添加轴标签
plt.xlabel('月  份')
plt.ylabel('货物量(万吨)')
# 添加标题
plt.title('2017年各月份物流运输量')
# 添加刻度标签
plt.xticks(np.arange(8),data.columns[1:])
# 设置Y轴的刻度范围
plt.ylim([0,500000])

# 为每个条形图添加数值标签
for x_t,y_t in enumerate(data.loc[0,:][1:]):
    plt.text(x_t,y_t/2,'%sW' %(round(y_t/10000,2)),ha='center', color = 'white')

for x_g,y_g in enumerate(data.loc[0,:][1:]+data.loc[1,:][1:]):
    plt.text(x_g,y_g/2,'%sW' %(round(y_g/10000,2)),ha='center', color = 'white')

for x_s,y_s in enumerate(data.loc[0,:][1:]+data.loc[1,:][1:]+data.loc[2,:][1:]):
    plt.text(x_s,y_s-20000,'%sW' %(round(y_s/10000,2)),ha='center', color = 'white')

# 显示图例
plt.legend(loc='upper center', ncol=4)
# 显示图形
plt.show()



























hist(v, main, xlab, xlim, ylim, breaks, col, border)
以下是所使用的参数的描述 -
    v       是保护直方图中使用的数值的向量
    main    表示图标的标题
    col     用于设置条的颜色
    border  用于设置每个条的边框颜色
    xlab    用于给出 x轴的描述(lab label)
    ylab    用于指定 y轴的描述
    xlim    用于指导 x轴上值的范围(lim limit)
    ylim    用于指定 y轴上值的范围
    break   用于提及每个条的宽度
    alpha   指定颜色透明度( install.packages('ggplot2') )
