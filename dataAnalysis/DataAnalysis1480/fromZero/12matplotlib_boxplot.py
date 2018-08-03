# matplotlib_boxplot
# E:/Documents/GitHub/MyCloud/dataAnalysis/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/


# 针对离散变量我们可以使用常见的条形图和饼图完成数据的可视化工作，那么，针对数值型变量，我们也有很多可视化的方法，例如箱线图、直方图、折线图、面积图、散点图等等

# 百度百科：
# 箱形图（Box-plot）又称为盒须图、盒式图或箱线图，是一种用作显示一组数据分散情况资料的统计图。因形状如箱子而得名。
# 在各种领域也经常被使用，常见于品质管理。它主要用于反映原始数据分布的特征，还可以进行多组数据分布特征的比较。
# 箱线图的绘制方法是：先找出一组数据的最大值、最小值、中位数和两个四分位数；然后， 连接两个四分位数画出箱子；再将最大值和最小值与箱子相连接，中位数在箱子中间。


# boxplot函数的参数解读
plt.boxplot(x, notch=None, sym=None, vert=None, whis=None, positions=None, widths=None,
            patch_artist=None, meanline=None, showmeans=None, showcaps=None, showbox=None,
            showfliers=None, boxprops=None, labels=None, flieprops=None, medianprops=None,
            meanprops=None, capprops=None, whiskerprops=None)

    x               指定要绘制箱线图的数据
    notch           是否是凹口的形式展现箱线图，默认非凹口
    sym             指定异常点的形状，默认为+号显示
    vert            是否需要将箱线图垂直摆放，默认垂直摆放
    whis            指定上下须与上下四分位数的距离，默认为1.5倍的四分位差
    positions       指定箱线图的位置，默认为[0,1,2...]
    widths          指定箱线图的宽度，默认为0.5
    patch_artist    是否填充箱体的颜色
    meanline        是否用线的形式表示均值，默认用点来表示
    showmeans       是否显示均值，默认不显示
    showcaps        是否显示箱线图顶端和末端的两条线，默认显示
    showbox         是否显示箱线图的箱体，默认显示
    showfliers      是否显示异常值，默认显示
    boxprops        设置箱体的属性，如边框色，填充色等
    labels          为箱线图添加标签，类似于图例的作用
    flierprops      设置异常值的属性，如异常点的形状、大小、填充色等
    medainprops     设置中位数的属性，如线的类型、粗细等
    meanprops       设置均值的属性，如点的大小、颜色等
    capprops        设置箱线图顶端和末端线条的属性，如颜色、粗细等
    whiskerprops    设置的属性，如颜色、粗细、线的类型等

# 箱线图的绘制

# 案例：titanic：不同等级仓位的年龄箱线图
# 整体乘客的年龄箱线图

# 导入第三方模块
import pandas as pd
import matplotlib.pyplot as plt

# 读取 Titanic 数据集
titanic = pd.read_csv('F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/matplotlab_titanic_dataset.csv')
# 检查年龄是否有缺失
any(titanic.age.isnull())
# 不妨删除含有缺失年龄的观察
titanic.dropna(subset=['age'], inplace=True)

# 设置图形的显示风格
plt.style.use('ggplot')

# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘图：整体乘客的年龄箱线图
plt.boxplot(x = titanic.age,    # 指定绘图数据
            patch_artist=True,  # 要求用自定义颜色填充盒型图，默认白色填充
            showmeans=True,     # 以点的形式显示均值
            boxprops={'color':'black', 'facecolor':'#9999ff'},   # 设置箱体属性，填充色和边框色
            flierprops={'marker': 'o', 'markerfacecolor': 'red', 'color':'black'},  # 设置异常值属性，点的形状、填充色和边框色
            meanprops={'marker': 'D', 'markerfacecolor': 'indianred'},      # 设置均值点的属性，点的形状、填充色
            medianprops={'linestyle': '--', 'color': 'orange'}  # 设置中位数线的属性，线的类型和颜色
)

# 设置y轴的范围
plt.ylim(0,85)

# 去除箱线图的上边框与有边框的刻度标签
plt.tick_params(top=False, right=False)
# 显示图形
plt.show()



# 不同等级的年龄箱线图

# 按舱级排序，为了后面正常显示分组盒型图的顺序
titanic.sort_values(by = 'pclass', inplace=True)

# 通过 for循环将不同仓位的年龄人群分别存储到列表 Age变量中
Age = []
Levels = titanic.pclass.unique()
for pclass in Levels:
    Age.append(titanic.loc[titanic.pclass==pclass, 'age'])

# 绘图
plt.boxplot(x = Age,
            patch_artist=True,
            labels=['一等舱','二等舱','三等舱'],   # 添加具体的标签名称
            showmeans=True,
            boxprops={'color': 'black', 'facecolor':'#9999ff'},
            flierprops={'marker':'o', 'markerfacecolor': 'red', 'color': 'block'},
            meanprops={'marker': 'D', 'markerfacecolor': 'indianred'},
            medianprops={'linestyle': '--', 'color': 'orange'}
)

# 显示图形
plt.show()
