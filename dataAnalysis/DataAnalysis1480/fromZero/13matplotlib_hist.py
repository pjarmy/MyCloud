# matplotlib_hist
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/


plt.hist(x, bins=10, range=None, density=False, weights=None, cumulative=False, bottom=None,
        histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None,
        label=None, stacked=False)

    x               指定要绘制直方图的数据
    bins            指定直方图的个数
    range           指定直方图数据的上下界，默认包含绘图数据的最大值和最小值
    density         是否将直方图的频数转换成频率（'normed' kwarg is deprecated）
    weights         该参数可为每一个数据点设置权重
    cumulative      是否需要及时累计频数或频率
    bottom          可以为直方图的每个条形添加基准线，默认为0
    histtype        指定直方图的类型，默认为bar，除此还有'barstacked', 'step', 'stepfilled'
    align           设置条形边界值的对齐方式，默认为mid，除此还有'left'和'right'
    orientation     设置直方图的摆放方向，默认为垂直方向
    rwidth          设置直方图条形宽度的百分比
    log             是否需要对绘图数据进行log交换
    color           设置直方图的填充色
    label           设置直方图的标签，可通过legend展示其图例
    stacked         当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放

# 一元直方图绘制

# 案例：titanic数据集

# 导入第三方包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取Titanic数据集
titanic = pd.read_csv('E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/matplotlab_titanic_dataset.csv')
# 检查年龄是否有缺失any(titanic.age.isnull())
# 不妨删除含有缺失年龄的观测
titanic.dropna(subset=['age'], inplace=True)

# 设置图形的显示风格
plt.style.use('ggplot')
# 绘图：乘客年龄的频率直方图
plt.hist(titanic.age,       # 绘图数据
        bins=20,            # 指定直方图的条形数为20个
        color='steelblue',  # 指定填充色
        edgecolor='k',      # 指定直方图的边界色
        label='直方图')      # 为直方图呈现标签

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top=False, right=False)
# 显示图例
plt.legend()
# 显示图形
plt.show()


# 绘制累计频率直方图，设置5岁为组距

# 绘图：乘客年龄的累计频率直方图

plt.hist(titanic.age,       # 绘制数据
        bins = np.arange(titanic.age.min(), titanic.age.max(),5),       # 指定直方图的组距
        density = True,      # 设置为频率直方图
        cumulative = True,      # 累计直方图
        color = 'steelblue',    # 指定填充色
        edgecolor = 'k',        # 指定直方图的边界色
        label = '直方图'         # 为直方图呈现标签
        )

# 设置坐标轴标签和标题
plt.title('乘客年龄的评论累计直方图')
plt.xlabel('年龄')
plt.ylabel('累计频率')

# 去除图形顶部边界和有边界的刻度
plt.tick_params(top=False, right=False)

# 显示图例
plt.legend(loc = 'best')
# 显示图形
plt.show()


# 类似帕累托图，为了测试数据集是否近似服从正态分布，需要再绘制两条曲线
# 理论的正态分布曲线，核密度曲线。两条曲线越吻合，说明数据越近似正态分布

# 正态分布图
plt.hist(titanic.age,       # 绘图数据
        bins = np.arange(titanic.age.min(), titanic.age.max(), 5),      # 指定直方图的组距
        density = True,     # 设置为频率直方图
        color = 'steelblue',        # 指定填充色
        edgecolor = 'k'     # 指定直方图的边界色
        )

# 设置坐标轴标签和标题
plt.title('乘客年龄直方图')
plt.xlabel('年龄')
plt.ylabel('频率')

# 生成正态曲线的数据
x1 = np.linspace(titanic.age.min(), titanic.age.max(), 1000)
normal = mlab.normpdf(x1, titanic.age.mean(), titanic.age.std())
# 绘制正态分布曲线
line1, = plt.plot(x1, normal, 'r-', linewidth = 2)

# 生成核密度曲线的数据
kde = mlab.GaussianKDE(titanic.age)
x2 = np.linspace(titanic.age.min(), titanic.age.max(), 1000)
# 绘制
line2, = plt.plot(x2, kde(x2), 'g-', linewidth = 2)

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top=False, right=False)

# 显示图例
plt.legend([line1, line2], ['正态分布曲线', '核密度曲线'], loc='best')
# 显示图形
plt.show()

（从直方图展示来看，与力量正态分布曲线有差异，说明不服从正态分布。【呈现右偏的特征】）


# 二元直方图的绘制

# 上面绘制的都是基于所有乘客的年龄，如果想对比男女乘客的年龄直方图，我们可以通过两个hist将不同性别的直方图绘制到一直图内

# 提取不同性别的年龄数据
age_female = titanic.age[titanic.sex == 'female']
age_male = titanic.age[titanic.sex == 'male']

# 设置直方图的组距
bins = np.arange(titanic.age.min(), titanic.age.max(), 2)
# 男性乘客年龄直方图
plt.hist(age_male, bins = bins, label = '男性', color = 'steelblue', alpha = 0.7)
# 女性乘客年龄直方图
plt.hist(age_female, bins = bins, label = '女性', alpha = 0.7)

# 设置坐标轴标签和标题
plt.title('乘客年龄直方图')
plt.xlabel('年龄')
plt.ylabel('人数')

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top=False, right=False)

# 显示图例
plt.legend()
# 显示图形
plt.show()
