# matplotlib_plot
# E:/Documents/GitHub/MyCloud/dataAnalysis/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/

# 折线图：一般用来表示某个数值量随时间的推移而形成的趋势。如：经济走势、销售波动图、PV监控图等。
# 调用 plot()可以实现折线图的绘制。

# plot()参数解读

# matplotlib模块中 plot()语法集参数意义
plt.hist(x, y, linestyle,
        linewidth, color, marker, markersize, markeredgecolor,
        markerfactcolor, label, alpha)

    x                   # 指定折线图的 x轴数据
    y                   # 指定直线图的 y轴数据
    linestyle           # 指定折线的类型，可以是实线、虚线、点虚线、点点线等，默认文实线
    linewidth           # 指定折线的宽度
    marker              # 可以为折线图添加点，该参数是设置点的形状
    markersize          # 设置点的大小
    markeredgecolor     # 设置点的边框色
    markerfactcolor     # 设置点的填充色
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
article_reading = pd.read_excel('F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/matplotlib_wechart.xlsx')





































1
