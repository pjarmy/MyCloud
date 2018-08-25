# 28-29_Kcluster.py(K均值聚类)
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

#     聚类是一种无监督的挖掘算法，其目的就是将N个样本安装特定的划分为K个簇（K<N），而这个
# 簇所表现的特征是：簇内样本相似度高（方差小），而簇间的相似度低（方差大）。关于聚类算法有
# 很多，如 K均值聚类、密度聚类、谱系聚类、最大期望聚类等。

#     本文我们介绍的是 K均值聚类，它是公认的十大挖掘算法之一，其优点是计算速度快、原理易于
# 理解及聚类效果理想。

# 如何借助Python和R语言工具完成K均值聚类的实战。
# 实战数据来源于虎扑体育（https://nba.hupu.com/stats/players）
# 我们借助于NBA秋衣的名字率和罚球命中率两个来给各位球员做一次“人以群分”的效果

#     首先，我们使用 pandas中的 read_html函数读取虎扑体育网页中的球员数据表，然后再对数据
# 作清洗（主要是数据类型的转换、变量的重命名和观测的删除）：

# 加载第三方包
# !pip install lxml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# !pip install sklearn
from sklearn.cluster import KMeans

# 读取网页中的数据表
table = []
for i in range(1,7):
    table.append(pd.read_html('https://nba.hupu.com/stats/players/pts/%d' %i)[0])

# 所有数据纵向合并为数据框
players = pd.concat(table)
# 变量重命名
# columns = ['排名','球员','球队','得分','命中-出手','命中率','命中-三分','三分命中率',
#         '命中-罚球','罚球命中率','场次','上场时间']
# players.columns= columns

# 数据类型转换
players.得分 = players.得分.astype('float')
players.命中率 = players.命中率.str[:-1].astype('float')/100
players.三分命中率 = players.三分命中率.str[:-1].astype('floar')/100
players.罚球命中率 = players.罚球命中率.str[:-1].satype










































1
