# matplotlib_scatter(散点图)
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

# scatter()函数的参数解读

plt.scatter(x, y, s=20
            c=None, marker='o', cmap=None, norm=Norm, vmin=None,vmax=None,
            alpha=None, linewidths=None, edgecolors=None)

    x               指定散点图的 x轴数据
    y               指定散点图的 y轴数据
    s               指定散点图点的大小，默认为20，通过传入新的变量，实现气泡图的绘制
    c               指定散点图的颜色，默认为蓝色
    marker          指定散点图的形状，默认为圆形
    cmap            指定散点图点的形状，默认为圆形
    norm            设置数据亮度，标准化到0~1之间，如果使用了norm则该参数无效
    vimin、vmax      亮度设置，与norm类似，如果使用了 norm则该参数无效
    alpha           设置散点的透明度
    linewidths      设置散点边界线的宽度
    edgecolors      设置散点边界线的颜色


# 一般散点图的绘制

# 案列：汽车速度与刹车距离的关系

# 导入模块
import pandas as pd
import matplotlib.pyplot as plt

# 设置绘图风格（添加网格线）
plt.style.use('ggplot')
# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读入数据
cars = pd.read_csv('E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/matplotlib_cars.csv')
# 绘图
plt.scatter(cars.speed,         # x轴数据为汽车速度
            cars.dist,       # y轴数据为汽车的刹车距离
            s = 30,         # 设置点的大小
            c = 'steelblue',        # 设置点的颜色
            marker = 's',       # 设置点的形状
            alpha = 0.9,        # 设置点的透明度
            linewidths = 0.3,       # 设置散点边界的粗细
            edgecolor = 'red'       # 设置散点边界的颜色
            )

# 添加轴标签和标题
plt.title('汽车速度与刹车距离的关系')
plt.xlabel('汽车速度(km/h)')
plt.ylabel('刹车距离(米)')

# 设置横纵坐标范围
plt.xlim(0,30)
plt.ylim(-20,140)

# 去除图边框的顶部刻度和右边刻度
plt.tick_params(top=False, right=False)

# 显示图形
plt.show()

# 汽车的刹车速度与刹车距离存在正相关关系





# 分组散点图的绘制

# 案例： iris数据集

# 导入模块
import pandas as pd
import matplotlib.pyplot as plt

# 设置绘图风格
plt.style.use('ggplot')
# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
iris = pd.read_csv('E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/pandas_iris.csv')

# 自定义颜色
colors = ['steelblue','#9999ff','#ff9999']

# 三种不同的花品种S
pecies = iris.Name.unique()

# 通过循环的方式，完成分组散点图的绘制
for i in range(len(pecies)):
    plt.scatter(iris.loc[iris.Name == pecies[i], 'PetalLength'],
                iris.loc[iris.Name == pecies[i], 'PetalWidth'],
                s = 35, c = colors[i], label = pecies[i])

# 添加轴标签和标题
plt.title('花瓣长度与宽度的关系')
plt.xlabel('花瓣长度')
plt.ylabel('花瓣宽度')

# 设置横纵坐标范围
plt.xlim(0,8)
plt.ylim(-0.5,3.0)

# 去除图边框的顶部刻度和右边刻度
plt.tick_params(top=False, right=False)
# 添加图例
plt.legend(loc = 'upper left')
# 显示图例
plt.show()





# 气泡图的绘制

# 案例：大区销售数据

# 导入第三方包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
sales = pd.read_excel('E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/matplotlib_sales.xlsx')

# 绘制气泡图
plt.scatter(sales.finish_ratio,
            sales.profit_ratio,
            c = 'steelblue',
            s = sales.tot_target/30,
            edgecolor = 'black')

# 改变轴刻度的显示方式（百分比形式）
plt.xticks(np.arange(0,1,0.1), [str(i)+'%' for i in np.arange(0,100,10)])
plt.yticks(np.arange(0,1,0.1), [str(i)+'%' for i in np.arange(0,100,10)])

# 设置 x轴和 y轴的数据范围
plt.xlim(0.2, 0.7)
plt.ylim(0.25, 0.85)

# 添加轴标签和标题
plt.title('完成率与利润率的关系')
plt.xlabel('完成率')
plt.ylabel('利润率')

# 去除图边框的顶部刻度和右边刻度
plt.tick_params(top=False, right=False)
# 显示图例
plt.show()




# 散点图 + 线性回归线

# 汽车速度与刹车距离的关系

# 导入第三方模块
# !pip install sklearn
# !pip install scipy
from sklearn.linear_model import LinearRegression

# 导入数据
cars = pd.read_csv('E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/matplotlib_cars.csv')
# 散点图
plt.scatter(cars.speed,     # x轴数据为汽车速度
            cars.dist,      # y轴数据为汽车的刹车距离
            s = 30,         # 设置点的大小
            c = 'black',    # 设置点的颜色
            marker = 'o',   # 设置点的形状
            alpha = 0.9,    # 设置散点的透明度
            linewidths = 0.3,   # 设置散点边界的粗细
            label = '观测点'
            )

# 建模
reg = LinearRegression().fit(cars.speed.values.reshape(-1,1), cars.dist)
# 回归预测值
pred = reg.predict(cars.speed.values.reshape(-1,1))

# 绘制回归线
plt.plot(cars.speed, pred, linewidth = 2, label = '回归线')

# 添加轴标签和标题
plt.title('汽车速度与刹车距离的关系')
plt.xlabel('汽车速度')
plt.ylabel('刹车距离')

# 设置 x轴和 y轴的数据范围
plt.xlim(0, 30)
plt.ylim(-20, 140)

# 去除图边框的顶部刻度和右边刻度
plt.tick_params(top=False, right=False)
# 显示图例
plt.legend(loc = 'upper left')
# 显示图形
plt.show()
