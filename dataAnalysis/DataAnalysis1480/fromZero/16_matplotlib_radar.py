# matplotlib_radar(雷达图)
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

# 雷达图的绘制

# 导入第三方模块
import numpy as np
import matplotlib.pyplot as plt

# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置绘图风格
plt.style.use('ggplot')

# 构造数据
values = [3.2,2.1,3.5,2.8,3]
feature = ['个人能力','QC知识','解决问题能力','服务质量意识','团队意识']

N = len(values)
# 设置雷达图的角度，用于平方切开一个圆面
angles=np.linspace(0, 2*np.pi, N, endpoint=False)

# 为了使雷达图一圈封闭起来，需要下面的步骤
values=np.concatenate((values, [values[0]]))
angles=np.concatenate((angles,[angles[0]]))

# 绘图
fig = plt.figure()
# 这里一定要设置为极坐标格式
ax = fig.add_subplot(111, polar=True)
# 绘制折线图
ax.plot(angles, values, 'o-', linewidth=2)
# 填充颜色
ax.fill(angles, values, alpha=0.25)
# 添加每个特征的标签
ax.set_thetagrids(angles * 180/np.pi, feature)
# 设置雷达图的范围
ax.set_ylim(0,5)
# 添加标题
plt.title('活动前后员工状态表现')
# 添加网络线
ax.grid(True)
# 显示图形
plt.show()




# 绘制多条线的雷达图

# 导入第三方模块
import numpy as np
import matplotlib.pyplot as plt

# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 使用ggplot的绘图风格
plt.style.use('ggplot')

# 构造数据
values = [3.2,2.1,3.5,2.8,3]
values2 = [4,4.1,4.5,4,4.1]
feature = ['个人能力','QC知识','解决问题能力','服务质量意识','团队精神']

N = len(values)
# 设置雷达图的角度，用于平方切开一个圆面
angles=np.linspace(0, 2*np.pi, N, endpoint=False)
# 为了使雷达图一圈封闭起来，需要下面的步骤
values=np.concatenate((values, [values[0]]))
values2=np.concatenate((values2, [values2[0]]))
angles=np.concatenate((angles, [angles[0]]))

# 绘图
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)
# 绘制折线图
ax.plot(angles, values, 'o-', linewidth=2, label='活动前')
# 填充颜色
ax.fill(angles, values, alpha=0.25)
# 绘制第二条折线图
ax.plot(angles, values2, 'o-', linewidth=2, label='活动后')
ax.fill(angles, values2, alpha=0.25)

# 添加每个特征的标签
ax.set_thetagrids(angles * 180/np.pi, feature)
# 设置雷达图的范围
ax.set_ylim(0,5)
# 添加标题
plt.title('活动前后员工状态表现')

# 添加网格线
ax.grid(True)
# 设置图例
plt.legend(loc = 'best')
# 显示图形
plt.show()





# pygal()模块

# 导入第三方模块
# !pip install pygal
import pygal

# 调用 Radar这个类，并设置雷达图的填充，及数据范围
radar_chart = pygal.Radar(fill = True, range=(0,5))
# 添加雷达图的标题
radar_chart.title = '活动前后员工状态表现'
# 添加雷达图各项点的含义
radar_chart.x_labels = ['个人能力','QC知识','解决问题能力','服务质量意识','团队精神']

# 绘制两条雷达图区域
radar_chart.add('活动前', [3.2,2.1,3.5,2.8,3])
radar_chart.add('活动后', [4,4.1,4.5,4,4.1])

# 保存图形
radar_chart.render_to_file('F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/radar_chart.svg')
