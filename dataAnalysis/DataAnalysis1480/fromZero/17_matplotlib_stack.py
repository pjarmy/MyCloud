# matplotlib_stackplot(面积图)
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

# stackplot()函数语法及参数含义

stackplot(x, *args, **kwargs)
    x           指定面积图的 x轴数据
    *args       为可变参数，可以接受任意多的 y轴数据，即各个拆分的数据对象
    **kwargs    为关键字参数，可以通过传递其他参数来修饰面积图，如标签、颜色
可用关键参数：
    lanbels     以列表的形式传递每一刻面积图包含的标签，通过图例展现
    colors      设置不同的颜色填充面积图

# 案例分享

# 2017年的物流运量

# ========== Python3 + Jupyter ========== #
# 导入第三方模块
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置图形的显示风格
plt.style.use('ggplot')
# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
transport = pd.read_excel('E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/matplotlib_transport.xls')
# 获取数据框的前5行
transport.head()

# 折线图的 x变量值，即 Jan（一月份）到 Aug（八月份）8个值
N = np.arange(transport.shape[1]-1)

# 绘制拆分的折线图
labels = transport.Index
channel = transport.columns[1:]

for i in range(transport.shape[0]):
    plt.plot(N,     # 坐标
            transport.loc[i, 'Jan':'Aug'],     # y坐标
            label = labels[i],      # 添加标签
            marker = 'o',       # 给折线图添加圆形点
            linewidth = 2       # 设置线的宽度
            )

# 添加标题和坐标轴标签
plt.title('2017年各运输渠道的运输量')
plt.ylabel('运输量（万吨）')
# 修改 x轴的刻度标签
plt.xticks(N, channel)

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top=False, right=False)

# 显示图例（即显示 label的效果）
plt.legend(loc = 'best')
# 显示图形
plt.show()




# 面积图展现

x = N
# 将铁路运输、公路运输和水路运输各月的值提取出来，存储到 y1~y3
# 千万记得，提取出数据框的一列时，需要将序列的数据类型进行强制转换，否则会报错
y1 = transport.loc[0, 'Jan':'Aug'].astype('int')
y2 = transport.loc[1, 'Jan':'Aug'].astype('int')
y3 = transport.loc[2, 'Jan':'Aug'].astype('int')

# 定义各区块面积的含义
colors = ['#ff9999','#9999ff','#cc1234']

# 绘制面积图
plt.stackplot(x,    # x轴
            y1,y2,y3,       # 可变参数，接受多个y
            labels = labels,        # 定义各区块面积的含义
            colors = colors     # 设置各区块的填充色
            )

# 添加标题和坐标轴标签
plt.title('2017年各运输渠道的运输量')
plt.ylabel('累积运输量（万吨）')

# 修改 x轴的刻度
plt.xticks(N, channel)

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top=False, right=False)

# 显示图例（即显示labels的效果）
plt.legend(loc = 'upper left')
# 显示图形
plt.show()
