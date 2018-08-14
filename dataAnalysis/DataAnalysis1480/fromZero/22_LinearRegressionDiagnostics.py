# LinearRegression.py(线性回归)
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

# 数据来源【高炉煤气联合循环发电（CCPP）数据集】
# http://archive.ics.uci.edu/ml/datasets/combined+cycle+power+plant


# 线性检验

# 线性回归模型，首先要保证自变量与因变量之间存在线性关系。
# 如何判断线性关系型，我们可以通过图形或 Pearson相关系数来识别：

# 导入第三方包
import pandas as pd
import numpy as np
from patsy import dmatrices
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm
import scipy.stats as stats
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


# 数据读取
ccpp = pd.read_excel('F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/CCPP.xlsx')
ccpp.describe()

===========================================================================
                AT            V           AP           RH           PE
count  9568.000000  9568.000000  9568.000000  9568.000000  9568.000000
mean     19.651231    54.305804  1013.259078    73.308978   454.365009
std       7.452473    12.707893     5.938784    14.600269    17.066995
min       1.810000    25.360000   992.890000    25.560000   420.260000
25%      13.510000    41.740000  1009.100000    63.327500   439.750000
50%      20.345000    52.080000  1012.940000    74.975000   451.550000
75%      25.720000    66.540000  1017.260000    84.830000   468.430000
max      37.110000    81.560000  1033.300000   100.160000   495.760000
===========================================================================

# AT：温度     V：压力    AP：相对湿度     RH：排气量      PE：发电量


# 绘制各变量之间的散点图
sns.pairplot(ccpp)
plt.show()

# 从得出的散点图来看，似乎 AP（相对湿度）和 RH（排气量）与 PE（发电量）之间并不存在明细的线性关系，
# 具体我们还需要看一下 PE与其余变量之间的 Pearson相关系数值。

# 发电量与自变量之间的相关系数
ccpp.corrwith(ccpp.PE)

==================
AT   -0.948128
V    -0.869780
AP    0.518429
RH    0.389794
PE    1.000000
dtype: float64
==================

# 从返回结果来看，PE（发电量）与 AT（温度）和 V（压力）之间的相关系数还是蛮高的，
# 而 PE与 AP（相对湿度）和 RH（排气量）之间的相关系数就明细小很多。
#
# 一般情况下：
# 当 Pearson相关系数 低于0.4，则表明变量之间存在弱相关关系；
# 当 Pearson相关系数在0.4~0.6之间，则说明变量之间存在中毒相关关系；
# 当 Pearson相关系数在0.6以上时，则反映变量之间存在强相关关系。
#
# 经过对比发现，PE与 RH之间的为弱相关关系，故不考虑将该变量纳入模型。
#
# 另外，变量之间不存在线性关系并不代表不存在关系，可能是二次函数关系，对数关系等；
# 所以一般还需要进行检验和变量转换































1
