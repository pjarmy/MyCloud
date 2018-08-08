# matplotlib_plot(热力图)
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

# 绘制填充表格热力图

# 数据采集——气温数据

# 通过爬虫获取，上海9月份每天的最高气温。要对原始数据进行清洗

# 步骤一：数据采集

# ========== Python3 + Jupyter ========== #
# 导入所需的第三方包
# !pip install requests
# !pip install bs4
# !pip install Seaborn
import datetime
import calendar
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 采集数据
# *****************************************************************

# 上海 2017~ 2018年 某月份离散气温数据
# url_201709 = 'http://lishi.tianqi.com/shanghai/201709.html'
url_201807 = 'http://lishi.tianqi.com/shanghai/201807.html'

# 发送爬虫请求(.text将整个html代码取下来了)
# response_201709 = requests.get(url_201709).text
response_201807 = requests.get(url_201807).text
# 解析源代码（将）
# soup_201709 = BeautifulSoup(response_201709, 'html.parser')
soup_201807 = BeautifulSoup(response_201807, 'html.parser')
# 根据 HTML标记语言，查询目标标记下的数据
# datas_201709 = soup_201709.findAll('div', {'class':'tqtongji2'})[0].findAll('ul')[1:]
datas_201807 = soup_201807.findAll('div', {'class':'tqtongji2'})[0].findAll('ul')[1:]

# 抓取日期数据
# date_201709 = [i.findAll('li')[0].text for i in datas_201709]
date_201807 = [i.findAll('li')[0].text for i in datas_201807]
# 抓取最高温数据
# high_201709 = [i.findAll('li')[1].text for i in datas_201709]
high_201807 = [i.findAll('li')[1].text for i in datas_201807]
# low_201709 = [i.findAll('li')[2].text for i in datas_201709]
# low_201807 = [i.findAll('li')[2].text for i in datas_201807]

# 创建数据框
# df_201709 = pd.DataFrame({'date':date_201709, 'high':high_201709})
df_201807 = pd.DataFrame({'date':date_201807, 'high':high_201807})
# df_201709 = pd.DataFrame({'date':date_201709, 'high':high_201709, 'low':low_201709})
# df_201807 = pd.DataFrame({'date':date_201807, 'high':high_201807, 'low':low_201807})

# 变量类型
# df_201709.dtypes
df_201807.dtypes


# 数据整理
# *****************************************************************

# 将 date变量转换为日期类型
# df_201709.date = pd.to_datetime(df_201709.date)
df_201807.date = pd.to_datetime(df_201807.date)
# 将 high变量转换成数值型
# df_201709.high = df_201709.high.astype('int')
df_201807.high = df_201807.high.astype('int')
# df_201709.low = df_201709.low.astype('int')
# df_201807.low = df_201807.low.astype('int')

# 数据处理
# 由日期型数据衍生出 weekday
# df_201709['weekday'] = df_201709.date.apply(pd.datetime.weekday)
df_201807['weekday'] = df_201807.date.apply(pd.datetime.weekday)

# 由于日期型数据计算 week_of_month，即当前日期在本月中是第几周
# 由于没有现成的函数，这里自定义一个函数来计算 week_of_month
def week_of_month(tgtdate):
    # 由日期型参数 tgtdate计算该月的天数
    days_this_month = calendar.mdays[tgtdate.month]     # 通过循环当月的所有天数，找出第二周的第一个日期
    for i in range(1, days_this_month + 1):
        d = datetime.datetime(tgtdate.year, tgtdate.month, i)
        if d.day - d.weekday() > 0:
            startdate = d
            break
    # 返回日期所属月份的第一周
    return (tgtdate - startdate).days //7  +  1

# df_201709['week_of_month'] = df_201709.date.apply(week_of_month)
df_201807['week_of_month'] = df_201807.date.apply(week_of_month)
# df_201807['day'] = index+1
# df_201709.head()
df_201807.head()




# 填充热力图的绘制
# *****************************************************************

# 基于 matplotlib绘制热力图
# pivot_table()制作一个透视表

# ==================绘图前的数据整理=====================
# 构建数据表（日历）
# target_201709 = pd.pivot_table(data = df_201709.iloc[:,1:], values = 'high',
#                         index = 'week_of_month', columns = 'weekday')
target_201807 = pd.pivot_table(data = df_201807.iloc[:,1:], values = 'high',
                        index = 'week_of_month', columns = 'weekday')
# target_201709
target_201807


# 缺失值填充（不填充的话 pcolor函数无法绘制）
# target_201709.fillna(0, inplace=True)
target_201807.fillna(0, inplace=True)
# 删除表格的索引名称
# target_201709.index.name = None
target_201807.index.name = None
# 对索引排序（为了让“第一周”到“第五周”的刻度从 y轴的高到底显示）
# target_201709.sort_index(ascending=False, inplace=True)
target_201807.sort_index(ascending=False, inplace=True)


# # ======================开始绘图=========================
# # 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# plt.pcolor(target_201709,               # 指定绘图数据
#             cmap=plt.cm.Blues,          # 指定填充色
#             edgecolors = 'white'        # 指定单元格直接的边框色
#             )
#
# # 添加x轴和y轴刻度标签(加0.5是为了让刻度标签居中显示)
# plt.xticks(np.arange(7)+0.5,['周一','周二','周三','周四','周五','周六','周日'])
# plt.yticks(np.arange(5)+0.5,['第五周','第四周','第三周','第二周','第一周'])
#
# # 去除图形顶部边界和右边界的刻度
# plt.tick_params(top=False, right=False)
# # 添加标题
# plt.title('上海市2017年9月份每日最高气温分布图')
# # 显示图形
# plt.show()



# ======================开始绘图=========================
# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.pcolor(target_201807,               # 指定绘图数据
            cmap=plt.cm.Blues,          # 指定填充色
            edgecolors = 'white'        # 指定单元格直接的边框色
            )

# 添加x轴和y轴刻度标签(加0.5是为了让刻度标签居中显示)
plt.xticks(np.arange(7)+0.5,['周一','周二','周三','周四','周五','周六','周日'])
plt.yticks(np.arange(5)+0.5,['第五周','第四周','第三周','第二周','第一周'])

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top=False, right=False)
# 添加标题
plt.title('上海市2018年7月份每日最高气温分布图')
# 显示图形
plt.show()


# 注意事项
# 1、绘图用的数据，不能包含缺失值
# 2、最终的图例无法实现
# 3、不方便将具体的温度值显示在每个单元格内

# 借助seaborn中的heatmap重新绘制解决


# 填充热力图的绘制
# *****************************************************************
# 基于seaborn绘制热力图

# 通过透视图函数形成绘图数据
target_201807 = pd.pivot_table(data = df_201807.iloc[:,1:], values = 'high',
                        index = 'week_of_month', columns = 'weekday')

# 绘图
ax = sns.heatmap(target_201807,         # 指定绘图数据
                cmap=plt.cm.Blues,      # 指定填充色
                linewidths=.1,          # 设置每个单元方块的间隔
                annot=True              # 显示数值
                )

# 添加 x轴刻度标签（加0.5是为了让刻度标签居中显示）
plt.xticks(np.arange(7)+0.5, ['周一','周二','周三','周四','周五','周六','周日'])
# 可以将刻度标签置于顶部显示
# ax.xaxis.tick_top()

# 添加 y轴刻度标签
plt.yticks(np.arange(5)+0.5, ['第一周','第二周','第三周','第四周','第五周'])
# 旋转 y刻度0度，即水平显示
plt.yticks(rotation = 0)

# 设置标题和坐标轴标签
ax.set_title('上海市2017年9月份每日最高气温分布图')
ax.set_xlabel('')
ax.set_ylabel('')

# 显示图形
plt.show()




































1
