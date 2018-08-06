# matplotlib_plot
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

# 折线图：一般用来表示某个数值量随时间的推移而形成的趋势。如：经济走势、销售波动图、PV监控图等。
# 调用 plot()可以实现折线图的绘制。

# plot()参数解读

# matplotlib模块中 plot()语法集参数意义
plt.hist(x, y, linestyle,
        linewidth, color, marker, markersize, markeredgecolor,
        markerfacecolor, label, alpha)

    x                   # 指定折线图的 x轴数据
    y                   # 指定直线图的 y轴数据
    linestyle           # 指定折线的类型，可以是实线、虚线、点虚线、点点线等，默认文实线
    linewidth           # 指定折线的宽度
    marker              # 可以为折线图添加点，该参数是设置点的形状
    markersize          # 设置点的大小
    markeredgecolor     # 设置点的边框色
    markerfacecolor     # 设置点的填充色
    label               # 为折线图添加标签，类似于图例的作用

# 一元折线图的绘制

# 案例：每天进步一点点2015公众号文字阅读人数

# 导入模块
import pandas as pd
import matplotlib.pyplot as plt

# 设置绘图风格
plt.style.use('ggplot')

# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取需要绘图的数据
article_reading = pd.read_excel('F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/matplotlib_wechart.xlsx')
# 取出 8月份至 9月28日的数据
sub_data = article_reading.loc[article_reading.date >= '2017-08-01', :]

# 设置图框的大小
fig = plt.figure(figsize=(10,6))
# 绘图
plt.plot(sub_data.date,         # x轴数据
        sub_data.article_reading_cnts,      # y轴数据
        linestyle = '-',        # 折线类型
        linewidth = 2,          # 折线宽度
        color = 'steelblue',    # 折线颜色
        marker = 'o',           # 点的形状
        markersize = 6,         # 点的大小
        markeredgecolor = 'black',      # 点的边框色
        markerfacecolor = 'brown'       # 点的填充色
        )

# 添加标题和坐标轴标签
plt.title('公众号每天阅读人数趋势图')
plt.xlabel('日期')
plt.ylabel('人数')

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top=False, right=False)

# 为了避免 x轴日期刻度标签的重叠，设置 x轴刻度自动展开，并且 45度倾斜
fig.autofmt_xdate(rotation = 45)

# 显示图形
plt.show()




# 由于 x轴是日期型数据，当数据量一多的时候，就会导致刻度标签的重叠或拥挤
# 为防止重叠的产生，我们需要让日期型的 x轴刻度标签自动展现

# 刻度标签个性化展示

# 导入模块
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置图框的大小
fig = plt.figure(figsize=(10,6))
# 绘图
plt.plot(sub_data.date,         # x轴数据
        sub_data.article_reading_cnts,      # y轴数据
        linestyle = '-',        # 折线类型
        linewidth = 2,          # 折线宽度
        color = 'steelblue',    # 折线颜色
        marker = 'o',           # 点的形状
        markersize = 6,         # 点的大小
        markeredgecolor = 'black',      # 点的边框色
        markerfacecolor = 'steelblue'       # 点的填充色
        )

# 添加标题和坐标轴标签
plt.title('公众号每天阅读人数趋势图')
plt.xlabel('日期')
plt.ylabel('人数')

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top=False, right=False)

# 获取图的坐标信息
ax = plt.gca()
# 设置日期的显示格式
date_format = mpl.dates.DateFormatter("%m-%d %Y")
ax.xaxis.set_major_formatter(date_format)

# 设置 x轴显示多少个日期刻度
# xlocator = mpl.ticker.MultipleLocator(5)
# 设置 x轴每个刻度间隔天数
xlocator = mpl.ticker.MultipleLocator(5)
ax.xaxis.set_major_locator(xlocator)

# 为了避免 x轴日期刻度标签的重叠，设置 x轴刻度自动展现，并且 45度倾斜
fig.autofmt_xdate(rotation = 45)

# 显示图形
plt.show()




# 多元折线图的绘制

# 一张图形中画上两条折线图

# 设置图框的大小
fig = plt.figure(figsize=(10,6))

# 绘图--阅读人数趋势
plt.plot(sub_data.date,     # x轴数据
        sub_data.article_reading_cnts,      # y轴数据
        linestyle = '-',        # 折线类型
        linewidth = 2,      # 折线宽度
        color = 'steelblue',        # 折线颜色
        marker = 'o',       # 点的形状
        markersize = 6,     # 点的大小
        markeredgecolor = 'black',      # 点的边框色
        markerfacecolor = 'steelblue',      # 点的填充色
        label = '阅读人数'      # 添加标签
        )

# 绘图--阅读人次趋势
plt.plot(sub_data.date,     # x轴数据
        sub_data.article_reading_times,      # y轴数据
        linestyle = '-',        # 折线类型
        linewidth = 2,      # 折线宽度
        color = '#ff9999',        # 折线颜色
        marker = 'o',       # 点的形状
        markersize = 6,     # 点的大小
        markeredgecolor = 'black',      # 点的边框色
        markerfacecolor = '#ff9999',      # 点的填充色
        label = '阅读人数'      # 添加标签
        )

# 添加标题和坐标轴标签
plt.title('公众号每天阅读人数趋势图')
plt.xlabel('日期')
plt.ylabel('人数')

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top=False, right=False)

# 获取图的坐标信息
ax = plt.gca()
# 设置日期的显示格式
date_format = mpl.dates.DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_format)

# 设置 x轴显示多少个日期刻度
# xlocator = mpl.ticker.MultipleLocator(10)
# 设置 x轴每个刻度间隔天数
xlocator = mpl.ticker.MultipleLocator(3)
ax.xaxis.set_major_locator(xlocator)

# 为了避免 x轴日期刻度标签的重叠，设置 x轴刻度自动展现，并且 45度倾斜
fig.autofmt_xdate(rotation = 45)

# 显示图例
plt.legend()
# 显示图形
plt.show()
