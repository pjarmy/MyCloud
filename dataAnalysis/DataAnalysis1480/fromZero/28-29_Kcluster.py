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
# !pip install lxml 重启 ipython
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# !pip install sklearn
from sklearn.cluster import KMeans

# 读取网页中的数据表
table = []
for i in range(1,7):
    table.append(pd.read_html('https://nba.hupu.com/stats/players/pts/%d' %i)[0].iloc[1:,])

# 所有数据纵向合并为数据框
players = pd.concat(table)
# 变量重命名
columns = ['排名','球员','球队','得分','命中-出手','命中率','命中-三分','三分命中率',
        '命中-罚球','罚球命中率','场次','上场时间']
players.columns= columns

# 数据类型转换，分开执行，players.dtypes
players.得分 = players.得分.astype('float')
players.命中率 = players.命中率.str[:-1].astype('float')/100
players.三分命中率 = players.三分命中率.str[:-1].astype('float')/100
players.罚球命中率 = players.罚球命中率.str[:-1].astype('float')/100
players.场次 = players.场次.astype('int')
players.上场时间 = players.上场时间.astype('float')

# 删除行标签为 0 的记录
# players.drop(0, inplace=True)
players.head()

'''===========================================================================================================================
  排名         球员  球队    得分        命中-出手    命中率      命中-三分  三分命中率      命中-罚球  罚球命中率  场次  上场时间
1  1    勒布朗-詹姆斯  湖人  33.2  12.30-22.50  0.547  1.60-5.10  0.309  7.00-9.60  0.732  16  40.6
2  2    安东尼-戴维斯  鹈鹕  30.1  11.80-22.70  0.520  0.70-2.40  0.273  5.90-7.10  0.828   9  39.8
3  3  拉塞尔-威斯布鲁克  雷霆  29.3  10.70-26.80  0.398  2.50-7.00  0.357  5.50-6.70  0.825   6  39.2
4  4     凯文-杜兰特  勇士  29.1  10.50-21.40  0.492  2.10-6.70  0.309  6.00-6.50  0.923  14  37.3
5  5     詹姆斯-哈登  火箭  28.8   9.40-22.20  0.421  3.30-9.90  0.333  6.80-7.60  0.888  14  35.6
==========================================================================================================================='''

#     本次一共获得 286名球员的历史投篮记录，这些记录包括球员姓名、所属球队、得分、各命中率
# 等信息，下面我们仅使用球员的命中率和罚球命中率来做聚类，主要是为了方便展现聚类效果。首先，
# 我们来看看这两个指标下的散点图：

# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 设置绘图风格
plt.style.use('ggplot')

# 绘制得分与命中率的散点图
players.plot(x='罚球命中率', y='命中率', kind='scatter')
plt.show()


#     通过肉眼，似乎还无法对这 50名球员进行聚类（花圈），如果花圈的话，该划为几类合适呢？
# 一般我们可以通过迭代的方式选出合适的聚类个数，即让 k值从 1到 K一次执行一遍，再看每一次
# k值对应的簇内离差平方和之和的变化，如果变化幅度突然由大转小时，那个 k值就是我们选择的合理
# 个数。具体我们通过图形展现来说明上面的文字：

# 选择最佳的 K值
X = players[['罚球命中率','命中率']]
K = range(1, int(np.sqrt(players.shape[0])))
GSSE = []
for k in K:
    SSE = []
    kmeans = KMeans(n_clusters=k, random_state=10)
    kmeans.fit(X)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_
    for label in set(labels):
        SSE.append(np.sum(np.sum((players[['罚球命中率','命中率']].loc[labels == label,]-centers[label,:])**2)))
    GSSE.append(np.sum(SSE))

# 绘制 K的个数与 GSSE的关系
plt.plot(K, GSSE, 'b*-')
plt.xlabel('聚类个数')
plt.ylabel('簇内离差平方和')
plt.title('选择最优的聚类个数')
plt.show()


#     从图中结果显示，当k值为5是，看上去簇内离差平方和之和的变化已慢慢变小，那么，我们不妨
# 就将球员聚为 7类。如下为聚类效果的代码：

# 调用 sklearn的库函数
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, random_state=1)
kmeans.fit(X)

# 聚类结果标签
players['cluster'] = kmeans.labels_
# 聚类中心
centers = kmeans.cluster_centers_

# 绘制散点图
plt.scatter(x = X.iloc[:,0], y = X.iloc[:,1], c = players['cluster'], s=50, cmap='rainbow')
plt.scatter(centers[:,0], centers[:,1], c='k', marker = '*', s = 180)
plt.xlabel('罚球命中率')
plt.ylabel('命中率')
# 图形显示
plt.show()


# 数据的空值检测
players.isnull().sum()

'''================
排名       0
球员       0
球队       1
得分       0
命中-出手    0
命中率      0
命中-三分    0
三分命中率    0
命中-罚球    0
罚球命中率    0
场次       0
上场时间     0
dtype: int64
================'''


# pandas数据处理 https://blog.csdn.net/sxf1061926959/article/details/56280759
players_fillna = players.fillna(u'自由球员')

# 保存数据到本地
# !pip install openpyxl
# pandas保存为 excel、csv： https://blog.csdn.net/yanqianglifei/article/details/77738476
# pandas to_csv最左边 多一列 的问题： https://blog.csdn.net/guotong1988/article/details/80513879
players_fillna.to_excel('F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/players.xlsx', index=False)
players_fillna.to_csv('F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/players1.csv', index=False)
# python导出的csv不可用，需要excel或者csv重新保存一下


#     上图中，散点的不同颜色表示的是聚为不同的簇，黑色五角星为各簇的中心点，看上去其聚类效
# 果有那么点意思。到此，关于使用 Python实现 K均值聚类的实战我们就分享到这里，接下来将使用
# R语言重新重复一遍，希望对 R语言熟悉的朋友有一点的帮助。如下是 R语言的复现脚本：

# # # # # # # # # # # # # # # # # # # # # # # #
# R 语言
# # # # # # # # # # # # # # # # # # # # # # # #

# 加载第三方包
library(ggplot2)

# 读取 Python中现成下好的数据
columns = c('排名','球员','球队','得分','命中-出手','命中率','命中-三分','三分命中率',
        '命中-罚球','罚球命中率','场次','上场时间')
# 需要把 players.csv 或 players.xlsx 另存为 csv文件，再保存一下
players = read.csv(file = file.choose())
# players = read_excel(path = 'F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/players.xlsx')
head(players)

# 绘制罚球命中率和命中率散点图
ggplot(data = players, mapping = aes(x = 罚球命中率, y = 命中率)) + geom_point()

# 自定义函数选择最佳的 K值
tot.wssplot <- function(data, nc, seed=1234){
    # 假设分为一组时的总的离差平方和
    tot.wss <- (nrow(data)-1)*sum(apply(data,2,var))
    for (i in 2:nc){
        # 必须指定随机种子数
        set.seed(seed)
        tot.wss[i] <- sum(kmeans(data, centers=i)$withinss)
    }
    ggplot(data = NULL, mapping = aes(x = 1:nc, y = tot.wss)) +
        geom_point() +
        geom_line(color = 'steelblue',size = 1) +
        labs(x = '聚类个数', y = '簇内离差平方和', title = '选择最优的聚类个数') +
        theme(plot.title = element_text(hjust = 0.5, face = 'bold'))
    }

# 绘制各种数组下的总的组内平方和图
tot.wssplot(data = players[, c('罚球命中率', '命中率')],
            nc = as.integer(sqrt(nrow(players))))

# 聚类
clust <- kmeans(x = players[, c('罚球命中率', '命中率')], centers = 7)
centers = clust$centers
players$cluster = clust$cluster

# 聚类效果图
ggplot() +
    geom_point(data = players,
            mapping = aes(x = 罚球命中率, y = 命中率, color = factor(cluster)), size = 1.5) +
    geom_point(aes(x = centers[,1], y = centers[,2]),
            fill = 'black', shape = 18, size =3)
    labs(title = '聚类效果图')
    theme(plot.title = element_text(hjust=0.5, face='bold'), legend.position="none")






































1
