# matplotlib_pie
# E:/Documents/GitHub/MyCloud/dataAnalysis/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/fromZero/data/

# pie函数参数解读
plt.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6,
        shadow=False, labeldistance=1.1, startangle=None, radius=None,
        couunterclock=True, wedgeprops=None, textprops=None, center=(0,0), frame=False)

    x               指定绘图的数据；
    explode         指定饼图某些部分的突出显示，即呈现爆炸式；
    labels          为饼图添加说明，类似于图例说明
    colors          指定饼图的填充颜色；
    autopct         自动添加百分比显示，可以采用格式化的方法显示；
    pctdistance     设置百分比标签与圆心的距离
    shadow          是否添加饼图阴影效果
    labeldistance   设置各扇形标签（图例）与圆心的距离；
    startangle      设置饼图初始摆放角度；
    radius          设置饼图半径大小；
    couunterclock   是否让饼图按逆时针顺序呈现；
    wedgeprops      设置饼图内外边界属性，如边界线的粗细，颜色等；
    textprops       设置饼图中文本的属性，如字体大小，颜色等；
    center          值饼图的中心点位置，默认为元点
    frame           是否要显示饼图背后的图框，如果设置为True的话，需要同时控制图框x轴、y轴的范围和饼图的中心地位


# 饼图的绘制
# 案例：芝麻信用失信用户分析

# 芝麻信用近300W失信人群样本统计数据，从受教育水平上看
# 中专：25.15%   大专：37.24%   本科：33.36%   硕士：3.68%

# 导入第三方模块
import matplotlib.pyplot as plt

# 设置绘图的主题风格（使用R中的ggplot分隔）
plt.style.use('ggplot')

# 构造数据
edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
labels = ['中专','大专','本科','硕士','其他']

explode = [0,0.1,0,0,0]     # 用于突出显示大专学历人群
colors=['#9999ff','#ff9999','#7777aa','#2442aa','#dd5555']     # 自定义颜色

# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 将横、纵坐标轴标准化处理，保证拼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')

# 控制x轴和y轴的范围
plt.xlim(0,4)
plt.ylim(0,4)

# 绘制饼图
plt.pie(x = edu,    # 绘图数据
        explode = explode,      # 突出显示大专人群
        labels = labels,        # 添加教育水平标签
        colors = colors,        # 设置饼图的自定义填充色
        autopct = '%.1f%%',     # 设置百分比的个数，这里保留一位小数
        pctdistance = 0.8,       # 设置百分比标签与圆心的距离
        labeldistance = 1.15,    # 设置教育水平标签与圆心的距离
        startangle = 180,       # 设置饼图的初始角度
        radius = 1.5,       # 设置饼图的半径
        counterclock = False,      # 是否逆时针，这里设置为顺时针方向
        wedgeprops = {'linewidth': 1.5, 'edgecolor': 'green'},      # 设置饼图内外边界的属性值
        textprops = {'fontsize': 12, 'color': 'k'},     # 设置文本标签的属性值
        center =(1.8, 1.8),      # 设置饼图的原点
        frame = 1 )     # 是否显示饼图的图框，这里设置显示

# 删除x轴和y轴的刻度
plt.xticks(())
plt.yticks(())
# 添加图标题
plt.title('芝麻信用失信用户教育水平分布')

# 显示图形
plt.show()




























1
