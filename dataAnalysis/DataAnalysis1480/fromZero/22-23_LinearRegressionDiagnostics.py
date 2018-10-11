# LinearRegression.py(线性回归诊断)
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

# 数据来源【高炉煤气联合循环发电（CCPP）数据集】
# http://archive.ics.uci.edu/ml/datasets/combined+cycle+power+plant



# # # # # # # # # # # # # # # # # # # # # # # #
# 线性检验
# # # # # # # # # # # # # # # # # # # # # # # #


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
ccpp = pd.read_excel('E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/CCPP.xlsx')
ccpp.describe()

'''===========================================================================
                AT            V           AP           RH           PE
count  9568.000000  9568.000000  9568.000000  9568.000000  9568.000000
mean     19.651231    54.305804  1013.259078    73.308978   454.365009
std       7.452473    12.707893     5.938784    14.600269    17.066995
min       1.810000    25.360000   992.890000    25.560000   420.260000
25%      13.510000    41.740000  1009.100000    63.327500   439.750000
50%      20.345000    52.080000  1012.940000    74.975000   451.550000
75%      25.720000    66.540000  1017.260000    84.830000   468.430000
max      37.110000    81.560000  1033.300000   100.160000   495.760000
==========================================================================='''

# AT：温度     V：压力    AP：相对湿度     RH：排气量      PE：发电量


# 绘制各变量之间的散点图
sns.pairplot(ccpp)
plt.show()

# 从得出的散点图来看，似乎 AP（相对湿度）和 RH（排气量）与 PE（发电量）之间并不存在明细的线性关系，
# 具体我们还需要看一下 PE与其余变量之间的 Pearson相关系数值。

# 发电量与自变量之间的相关系数
ccpp.corrwith(ccpp.PE)

'''==================
AT   -0.948128
V    -0.869780
AP    0.518429
RH    0.389794
PE    1.000000
dtype: float64
=================='''

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



# # # # # # # # # # # # # # # # # # # # # # # #
# 多重共线性检验
# # # # # # # # # # # # # # # # # # # # # # # #


# 如果模型的自变量之间存在严重的多重共线性，会导致的后果：

# 导致 OLS估计量可能无效；
# 增大 OLS估计量的方差
# 变量的显著性检验将失去意义；
# 模型缺乏稳定性；

# 所以多重线性检验就显得非常重要了，关于多重共线性的检验可以使用方差膨胀因子（VIF）来鉴定，
# 如果 VIF大于10，则说明变量存在多重共线性。
# 一旦发现变量之间存在多重共线性的话，可以考虑删除变量和重新选择模型（岭回归法）

# 百度百科
# 方差膨胀因子（Variance Inflation Factor，VIF）：是指解释变量之间存在多重共线性时的方差与不存在
# 多重共线性时的方差之比。容忍度的倒数，VIF越大，显示共线性越严重。经验判断方法表明：当0<VIF<10，
# 不存在多重共线性；当10=<VIF<100，存在较强的多重共线性；当VIF>=100，存在严重的多重共线性。
# 多重共线性，有机会研究。


# 将因变量 PE，自变量 AT， V， AP和截距项（值为1的1维数组）以数据框的形式组合起来
y, X = dmatrices('PE~AT+V+AP', data = ccpp, return_type='dataframe')

# 构造空的数据框
vif = pd.DataFrame()
# 定义空数据框的两个列
vif["VIF Factor"] =[variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns
vif

'''===============================
     VIF Factor   features
0  39847.945838  Intercept
1      3.888380         AT
2      3.482090          V
3      1.348401         AP
==============================='''

# 结果显示，所有自变量的 VIF 均低于 10，说明自变量之间并不存在多重线性的隐患。



# # # # # # # # # # # # # # # # # # # # # # # #
# 异常点检测
# # # # # # # # # # # # # # # # # # # # # # # #

# 在异常点检测之前，我们需要对现有的数据，进行线性回归模型的构造。具体操作如下：

# 构造 PE与 AT、V 和 AP之间的线性模型
fit = sm.formula.ols('PE~AT+V+AP', data = ccpp).fit()
fit.summary()

'''===================================================================================
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results
==============================================================================
Dep. Variable:                     PE   R-squared:                       0.918
Model:                            OLS   Adj. R-squared:                  0.918
Method:                 Least Squares   F-statistic:                 3.568e+04
Date:                Wed, 15 Aug 2018   Prob (F-statistic):               0.00
Time:                        10:07:40   Log-Likelihood:                -28758.
No. Observations:                9568   AIC:                         5.752e+04
Df Residuals:                    9564   BIC:                         5.755e+04
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    344.0714      9.977     34.487      0.000     324.515     363.628
AT            -1.6348      0.013   -123.613      0.000      -1.661      -1.609
V             -0.3283      0.007    -44.735      0.000      -0.343      -0.314
AP             0.1582      0.010     16.183      0.000       0.139       0.177
==============================================================================
Omnibus:                      542.551   Durbin-Watson:                   2.024
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             1896.378
Skew:                          -0.198   Prob(JB):                         0.00
Kurtosis:                       5.145   Cond. No.                     2.03e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.03e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
==================================================================================='''


from sklearn.metrics import mean_squared_error
pred = fit.predict()
np.sqrt(mean_squared_error(ccpp.PE, pred))

'''======================
4.887719834860165
======================'''

# 通过上面的建模结果来看，一切显得那么的完美（模型显著性检验通过，偏回归系数的显著性校验通过，
# R方值也达到了0.9以上）。尽管这样，我们还是需要基于这个模型，完成异常点的检测。


# 关于异常点检测方法，一般可以通过高杠杆值点（帽子矩阵）或 DFFITS值、学生化残差、cook距离
# 和 covratio值来判断。这些值的具体计算脚本如下：

# 离群点检测
outliers = fit.get_influence()

# 高杠杆指点（帽子矩阵）
leverage = outliers.hat_matrix_diag
# DFFITS值
dffits = outliers.dffits[0]
# 学生化残差
resid_stu = outliers.resid_studentized_external
# cook距离
cook = outliers.cooks_distance[0]
# covratio值
covratio = outliers.cov_ratio

# 将上面的几种异常值检验统计量与原始数据集合并
contat1 = pd.concat([pd.Series(leverage, name='leverage'), pd.Series(dffits, name='dffits'),
                    pd.Series(resid_stu, name='resid_stu'), pd.Series(cook, name='cook'),
                    pd.Series(covratio, name='covratio'),], axis = 1)
ccpp_outliers = pd.concat([ccpp, contat1], axis = 1)
ccpp_outliers.head()

'''===================================================================================================
      AT      V       AP     RH      PE  leverage    dffits  resid_stu          cook  covratio
0  14.96  41.76  1024.07  73.17  463.26  0.000549 -0.022075  -0.941799  1.218279e-04  1.000597
1  25.18  62.96  1020.04  59.08  444.37  0.000487  0.003668   0.166180  3.363110e-06  1.000894
2   5.11  39.40  1012.16  92.14  488.56  0.000787  0.032756   1.167083  2.682360e-04  1.000636
3  20.86  57.32  1010.24  76.64  446.48  0.000137 -0.010641  -0.908639  2.830953e-05  1.000210
4  10.82  37.50  1009.23  96.62  473.90  0.000514  0.001008   0.044471  2.542535e-07  1.000932
==================================================================================================='''


# 通过参考薛毅老师的《统计建模与R软件》书可知，
# 当高杠杆值点（或帽子矩阵）大于 2(p+1)/n 时，则认为该样本点可能存在异常（其中 p 为自变量的个数，n为观测的个数）；
# 当DFFITS统计值大于 2sqrt((p+1)/n)时，则认为该样本点可能存在异常；
# 当学生化残差的绝对值大于 2，则认为该样本点可能存在异常；
# 对于 cood距离来说，则没有明确的判断标准，一般来说，值越大则为异常点的可能性就越高；
# 对于 covratio值来说，如果一个样本的 covratio值离值 1 越远，则认为该样本越可能时异常值。
#
# 这里我们就以学生化残差作为评判标准，因为其包含了帽子矩阵和 DFFITS的信息



# 计算异常值数量的比例
outliers_ratio = sum(np.where((np.abs(ccpp_outliers.resid_stu)>2),1,0))/ccpp_outliers.shape[0]
outliers_ratio

'''======================
0.03710284280936455
======================'''

# 结果显示，确实存在异常值，且异常值的数量占了3.7%。对于异常值的处理，我们可以考虑下面几种方法
#
# 当异常比例极低时（5% 以内），可以考虑直接删除；
# 当异常比例比较高时，可以考虑将异常值衍生为哑变量，即异常值对应到1，非异常值则对应到0；
# 将单独把异常值提取出来，另行建模；
#
#
# 这里为了简单起见，我们将 3.7% 的异常值做删除处理：

# 删除异常值
ccpp_outliers = ccpp_outliers.loc[np.abs(ccpp_outliers.resid_stu)<=2,]


# 重新建模
fit2 = sm.formula.ols('PE~AT+V+AP', data = ccpp_outliers).fit()
fit2.summary()

'''===================================================================================
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results
==============================================================================
Dep. Variable:                     PE   R-squared:                       0.937
Model:                            OLS   Adj. R-squared:                  0.937
Method:                 Least Squares   F-statistic:                 4.550e+04
Date:                Wed, 15 Aug 2018   Prob (F-statistic):               0.00
Time:                        13:48:55   Log-Likelihood:                -26434.
No. Observations:                9213   AIC:                         5.288e+04
Df Residuals:                    9209   BIC:                         5.291e+04
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    349.8258      8.857     39.498      0.000     332.465     367.187
AT            -1.6719      0.012   -141.063      0.000      -1.695      -1.649
V             -0.3285      0.006    -50.545      0.000      -0.341      -0.316
AP             0.1531      0.009     17.647      0.000       0.136       0.170
==============================================================================
Omnibus:                      455.104   Durbin-Watson:                   1.992
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              184.929
Skew:                           0.058   Prob(JB):                     6.97e-41
Kurtosis:                       2.316   Cond. No.                     2.02e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.02e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
==================================================================================='''


pred2 = fit2.predict()
np.sqrt(mean_squared_error(ccpp_outliers.PE, pred2))

'''=======================
4.2644419500649375
======================='''

# 通过对比 fit 和 fit2，将异常值删除后重新建模的话，效果会更理想一点，具体表现为：
# 信息准则（AIC 和 BIC）均变小，同时RMSE（误差均方根） 也由原来的4.89降低到4.26




# # # # # # # # # # # # # # # # # # # # # # # #
# 正态性检验
# # # # # # # # # # # # # # # # # # # # # # # #

# 当模型的残差服从正态性假设时，才能保证模型偏回归系数对于t值和模型的F值时有效的。
# 故模型建好后，要对模型的残差进行正态性检验。关于正态性检验由两类方法，即定性圆形法
# （直方图，PP图和 QQ图）和定量的非参数法（Shapiro检验和 K-S检验）


# 残差的正态性检验（直方图法）
resid = fit2.resid

# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.hist(resid,         # 绘图数据
        bins = 100,     # 指定直方图条的个数
        density = True,  # 设置为频率直方图，normed弃用了
        color = 'steelblue',    # 指定填充色
        edgecolor = 'k')        # 指定直方图的边界色

# 设置坐标轴和标题
plt.title('残差直方图')
plt.ylabel('密度值')

# 生成正态曲线的数据
x1 = np.linspace(resid.min(), resid.max(), 1000)
normal = stats.norm.pdf(x1,resid.mean(), resid.std())
# mlab.normpdf弃用了   使用 scipy.stats.norm.pdf

# 绘制正态分布曲线
plt.plot(x1, normal, 'r-', linewidth = 2, label = '正态分布曲线')

# 生产核密度曲线的数据
kde = mlab.GaussianKDE(resid)
x2 = np.linspace(resid.min(), resid.max(), 1000)

# 绘制核密度曲线
plt.plot(x2, kde(x2), 'k-', linewidth = 2, label = '核密度曲线')

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top=False, right=False)

# 显示图例
plt.legend(loc='best')
# loc valid locations are
#         best
#         upper right
#         upper left
#         lower left
#         lower right
#         right
#         center left
#         center right
#         lower center
#         upper center
#         center

# 显示图形
plt.show()

# 从残差的直方图来看，核密度曲线与理论的正态分布曲线的趋势还是比较吻合的，即使残差不服从正态
# 分布，也额能反映其基本近似于正态分布。



# 残差的正态性检验（PP图和 QQ图法）
pp_qq_plot = sm.ProbPlot(resid)

pp_qq_plot.ppplot(line = '45')
plt.title('P-P图')

pp_qq_plot.qqplot(line = 'q')
plt.title('Q-Q图')

# 显示图形
plt.show()

# 从PP图和QQ图来看，有一部分样本点并没有落在参考线上，但绝大多数样本点还是与参考线保持一致的步调。


# 残差的正态性检验（非参数法）
standard_resid = (resid-np.mean(resid))/np.std(resid)
stats.kstest(standard_resid, 'norm')

'''===============================================================================
KstestResult(statistic=0.030784687051176818, pvalue=5.2151288608320515e-08)
==============================================================================='''

# 由于shapiro正态性检验对样本量的要求是5000以内；而本次数据集的样本量由9000多，故选择K-S
# 来完成正态性检验。从K-S检验的P值来看，拒绝了残差服从正态分布的假设，即认为残差并不满足正态
# 性假设这个潜艇。如果残差不服从正态分布的话，建议对Y变量进行box-cox变换处理。由于fit2模型的
# 残差并没有特别明显的偏态（偏度为0.058，接近于0），故这里就不对Y变量进行box-cox变换了。如果
# 需要变换的话，可以以下面的代码为例：

import scipy.stats as stats
# 找到box-cox变换的lambda系数
lamd = stats.boxcox_normmax(your_data_frame.y, method = 'mle')
# 对Y进行变换
your_data_frame['trans_y'] = stats.boxcox(your_data_frame.y, lamd)
# 建模
fit = sm.formula.ols('y~x1+x2+...', data = your_data_frame).fit()
fit.summary()

# 关于线性回归模型的异常点识别、线性性假设、无多重共线性假设和残差的正态性假设在Python中的
# 实现就介绍到这里。下一期，我们将针对线性回归模型残差的方差齐性和独立性假设进行讲解。







# 关于线性回归模型的另外两个假设前提的验证（即回归模型的残差满足齐性（即方差为某个固定值）
# 和残差之间互相独立性）。

# # # # # # # # # # # # # # # # # # # # # # # #
# 残差方差齐性检验
# # # # # # # # # # # # # # # # # # # # # # # #

# 在线性回归模型中，如果模型表现的非常好的话，那么残差与拟合值之间不应该存在某些明细的关系或趋势。
# 如果模型的残差确实存在一定的异方差的话，会导致估计出来的偏回归系数不具备有效性，甚至导致模型的预测也不准确。
# 所有，建模后需要验证残差方差是否具有齐性,检验的方法有两种:
# 一种时图示法，一种时统计验证法。具体代码如下：


# ====== 图示法完成方差齐性的判断 ======

# 标准化残差与预测值之间的散点图
plt.scatter(fit2.predict(), (fit2.resid-fit2.resid.mean())/fit2.resid.std())
plt.xlabel('预测值')
plt.ylabel('标准化残值')

# 添加水平参考线
plt.axhline(y =0, color = 'r', linewidth = 2)
plt.show()

# 从图中看，并没有发现明显的规律或趋势（判断标准：如果残差在参考线两次均匀分布，则意味着异方差性较弱；
# 而如果呈现出明显的不均匀分布，则意味着存在明显的异方差），故可以认为没有显著的异方差性特征。


# 除了上面的图示法，我们还可以通过White检验和Breush-Pagan检验来完成顶了化的异方差性检验，具体操作如下：

# ====== 统计法完成方差齐性的判断 ======
# White's Test
sm.stats.diagnostic.het_white(fit2.resid, exog = fit2.model.exog)
# Breusck-Pagan
sm.stats.diagnostic.het_breuschpagan(fit2.resid, exog_het = fit2.model.exog)
# `het_breushpagan` is deprecated, use `het_breuschpagan` instead!


'''===================================
(231.8632300336841,
 6.664951902732149e-45,     # P值
 26.399000490991146,
 1.7120704306927504e-45)

 (26.58307118758634,
 7.199522497313831e-06,     # P值
 8.882806882651435,
 7.101848974821258e-06)
 ==================================='''


# 从检验结果来看，不论时 White检验 还是 Breush-Pagan检验，P值都远远小于0.05这个判别界限，
# 即拒绝原假设（残差方差为常数的原假设），认为残差并不满足齐性这个假设。如果模型的残差趋势
# 不服从齐性的化，可以考虑两类方法来解决，一种时模型变换法，另一种时加权最小二乘法。

# 对于模型变换法来说，主要考虑残差与自变量之间的关系，
# 如果残差与某个自变量x成正比，则原始模型的两边需要同除以sqrt(x)；
# 如果残差与某个自变量x的平方成正比，则原始模型的两边需要同除以x。
# 对于加权最小二乘法来说，关键时如何确定权重，根据多方资料的搜索、验证，一般会选择如下三种权重来进行对比测试：

# 残差绝对值的倒数作为权重；
# 残差平方的倒数作为权重；
# 用残差的平方对数与X重新拟合建模，并将得到的拟合值取指数，用指数的倒数作为权重。


# 首先，我们通过图示法，用来观测自变量和残差之间的关系，来决定是否可以用模型变换来解决异方差问题：

# ===== 残差与x的关系 =====
plt.subplot(231)
plt.scatter(ccpp_outliers.AT, (fit2.resid-fit2.resid.mean())/fit2.resid.std())
plt.xlabel('AT')
plt.ylabel('标准化残差')
plt.axhline(color = 'red', linewidth = 2)

plt.subplot(232)
plt.scatter(ccpp_outliers.V, (fit2.resid-fit2.resid.mean())/fit2.resid.std())
plt.xlabel('V')
plt.ylabel('标准化残差')
plt.axhline(color = 'red', linewidth = 2)

plt.subplot(233)
plt.scatter(ccpp_outliers.AP, (fit2.resid-fit2.resid.mean())/fit2.resid.std())
plt.xlabel('AP')
plt.ylabel('标准化残差')
plt.axhline(color = 'red', linewidth = 2)

plt.subplot(234)
plt.scatter(np.power(ccpp_outliers.AT,2), (fit2.resid-fit2.resid.mean())/fit2.resid.std())
plt.xlabel('AT^2')
plt.ylabel('标准化残差')
plt.axhline(color = 'red', linewidth = 2)

plt.subplot(235)
plt.scatter(np.power(ccpp_outliers.V,2), (fit2.resid-fit2.resid.mean())/fit2.resid.std())
plt.xlabel('V^2')
plt.ylabel('标准化残差')
plt.axhline(color = 'red', linewidth = 2)

plt.subplot(236)
plt.scatter(np.power(ccpp_outliers.AP,2), (fit2.resid-fit2.resid.mean())/fit2.resid.std())
plt.xlabel('AP^2')
plt.ylabel('标准化残差')
plt.axhline(color = 'red', linewidth = 2)

# 设置子图之间的水平距离和高度间距
plt.subplots_adjust(hspace=0.3, wspace=0.3)
plt.show()


<<<<<<< HEAD
# 从图中结果可知，不管是自变量x本身，还是自变量x的平方，标准化残差都均匀的分布在参考线0腹肌，
# 并不成比例，故无法使用模型变换法。接下来我们尝试使用加权最小二乘法来解决问题：
=======
# 从图中结果可知，不管是自变量x本身，还是自变量x的平方，标准化残差都均匀的分布在参考线0附件，并不成比例，
# 股无法使用模型变换法。接下来我们尝试使用加权最小二乘法来解决问题。
>>>>>>> 0a0f04d06f12cb2f2b5366e8c5fa46cae2554ff4

# 三种权重
w1 = 1/np.abs(fit2.resid)
w2 = 1/fit2.resid**2
ccpp_outliers['loge2'] = np.log(fit2.resid**2)
# 第三种权重
model = sm.formula.ols('loge2~AT+V+AP', data = ccpp_outliers).fit()
w3 = 1/(np.exp(model.predict()))

<<<<<<< HEAD
# 建模
fit3 = sm.formula.wls('PE~AT+V+AP', data = ccpp_outliers, weights = w1).fit()
# 异方差检验
het3 = sm.stats.diagnostic.het_breuschpagan(fit3.resid, exog_het = fit3.model.exog)
# AIC
fit3.aic
=======
# 三种权重
w1 = 1/np.abs(fit2.resid)
w2 = 1/fit2.resid

>>>>>>> 0a0f04d06f12cb2f2b5366e8c5fa46cae2554ff4

fit4 = sm.formula.wls('PE~AT+V+AP', data = ccpp_outliers, weights = w2).fit()
het4 = sm.stats.diagnostic.het_breuschpagan(fit4.resid, exog_het = fit4.model.exog)
fit4.aic

fit5 = sm.formula.wls('PE~AT+V+AP', data = ccpp_outliers, weights = w3).fit()
het5 = sm.stats.diagnostic.het_breuschpagan(fit5.resid, exog_het = fit5.model.exog)
fit5.aic

# fit2模型
het2 = sm.stats.diagnostic.het_breuschpagan(fit2.resid, exog_het = fit2.model.exog)
fit2.aic


print('fit2模型异方差检验统计量：%.2f，P值为%.4f：' %(het2[0],het2[1]))
print('fit3模型异方差检验统计量：%.2f，P值为%.4f：' %(het3[0],het3[1]))
print('fit4模型异方差检验统计量：%.2f，P值为%.4f：' %(het4[0],het4[1]))
print('fit5模型异方差检验统计量：%.2f，P值为%.4f：\n' %(het5[0],het5[1]))

print('fit2模型的AIC：%.2f' %fit2.aic)
print('fit3模型的AIC：%.2f' %fit3.aic)
print('fit4模型的AIC：%.2f' %fit4.aic)
print('fit5模型的AIC：%.2f' %fit5.aic)

'''=============================================
fit2模型异方差检验统计量：26.58，P值为0.0000：
fit3模型异方差检验统计量：31.28，P值为0.0000：
fit4模型异方差检验统计量：26.74，P值为0.0000：
fit5模型异方差检验统计量：38.85，P值为0.0000：

fit2模型的AIC：52876.80
fit3模型的AIC：46016.14
fit4模型的AIC：42630.89
fit5模型的AIC：52857.92
============================================='''

通过对比发现，尽管我们采用了三种不同的权重，但都没能通过残差方差齐性的显著性检验，但似乎
fit4模型更加理性，相比于fit2来说，AIC信息更小（当然也可能产出过拟合问题）



# # # # # # # # # # # # # # # # # # # # # # # #
# 残差独立性检验
# # # # # # # # # # # # # # # # # # # # # # # #

# 之所以要求残差是独立的，说白了就是要求因变量y是独立的，因为在模型中只有y和残差项时变量，
# 而自变量X时已知的。如果再配合上正态分布的假设，那就是独立同分布于正态分布，关于残差的独立性
# 检验我们可以通过Durbin-Watson统计量来测试。其实，在模型的summary信息中就包含了残差的
# Durbin-Watson统计量值，如果该值越接近与2，则说明残差时独立的。一般而言，在实际的数据集中，
# 时间序列的样本之间可能存在相关性，而其他数据集之间基本还是独立的。

fit4.summary()

'''===================================================================================
<class 'statsmodels.iolib.summary.Summary'>
"""
                            WLS Regression Results
==============================================================================
Dep. Variable:                     PE   R-squared:                       1.000
Model:                            WLS   Adj. R-squared:                  1.000
Method:                 Least Squares   F-statistic:                 7.963e+07
Date:                Fri, 17 Aug 2018   Prob (F-statistic):               0.00
Time:                        11:09:34   Log-Likelihood:                -21311.
No. Observations:                9213   AIC:                         4.263e+04
Df Residuals:                    9209   BIC:                         4.266e+04
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    349.9863      0.256   1368.864      0.000     349.485     350.487
AT            -1.6723      0.000  -4831.713      0.000      -1.673      -1.672
V             -0.3283      0.000  -1666.503      0.000      -0.329      -0.328
AP             0.1530      0.000    621.177      0.000       0.152       0.153
==============================================================================
Omnibus:                        0.731   Durbin-Watson:                   2.003
Prob(Omnibus):                  0.694   Jarque-Bera (JB):             1534.329
Skew:                           0.022   Prob(JB):                         0.00
Kurtosis:                       1.001   Cond. No.                     1.24e+06
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.24e+06. This might indicate that there are
strong multicollinearity or other numerical problems.
"""
==================================================================================='''

# 从fit4模型的summary信息可知，Durbin-Waston统计量值几乎为2，故可以认为模型的残差之间是满足
# 独立性这个假设前提的。到此为止，我们就以fit4模型作为我们最终的确定模型，基于这个模型就可以
# 对新的数据集做预测。

# 下面对fit4模型产生的预测值和实际值作三点图，如果散点图与预测线特别紧密，则认为模型拟合的非常好

# 预测值与真实值的散点图
plt.scatter(fit4.predict(), ccpp_outliers.PE)
plt.plot([fit4.predict().min(), fit.predict().max()],
        [ccpp_outliers.PE.min(), ccpp_outliers.PE.max()],
        'r-', linewidth = 3)
plt.xlabel(u'预测值')
plt.ylabel(u'实际值')
# 显示图形
plt.show()













# 接下来我们再用R语言对上面的内容复现一遍

# # # # # # # # # # # # # # # # # # # # # # # #
# R语言脚本复现
# # # # # # # # # # # # # # # # # # # # # # # #

# 加载第三方包
# install.packages("GGally")
library(readxl)
library(GGally)

# 读取数据
ccpp <- read_excel(path = file.choose())
summary(ccpp)

# =====================================================================================
#        AT              V               AP               RH               PE
#  Min.   : 1.81   Min.   :25.36   Min.   : 992.9   Min.   : 25.56   Min.   :420.3
#  1st Qu.:13.51   1st Qu.:41.74   1st Qu.:1009.1   1st Qu.: 63.33   1st Qu.:439.8
#  Median :20.34   Median :52.08   Median :1012.9   Median : 74.97   Median :451.6
#  Mean   :19.65   Mean   :54.31   Mean   :1013.3   Mean   : 73.31   Mean   :454.4
#  3rd Qu.:25.72   3rd Qu.:66.54   3rd Qu.:1017.3   3rd Qu.: 84.83   3rd Qu.:468.4
#  Max.   :37.11   Max.   :81.56   Max.   :1033.3   Max.   :100.16   Max.   :495.8
# =====================================================================================


# 绘制各变量直接的散点图与相关系数
ggpairs(ccpp)


# 建模
fit <- lm(PE ~ AT + V + AP, data = ccpp)
summary(fit)

# =========================================================================
# Call:
# lm(formula = PE ~ AT + V + AP, data = ccpp)
#
# Residuals:
#     Min      1Q  Median      3Q     Max
# -44.063  -3.440  -0.073   3.319  19.449
#
# Coefficients:
#               Estimate Std. Error t value Pr(>|t|)
# (Intercept) 344.071387   9.976759   34.49   <2e-16 ***
# AT           -1.634777   0.013225 -123.61   <2e-16 ***
# V            -0.328323   0.007339  -44.73   <2e-16 ***
# AP            0.158152   0.009773   16.18   <2e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# Residual standard error: 4.889 on 9564 degrees of freedom
# Multiple R-squared:  0.918,	Adjusted R-squared:  0.9179
# F-statistic: 3.568e+04 on 3 and 9564 DF,  p-value: < 2.2e-16
# =========================================================================

RMSE = sqrt(mean(fit$residuals**2))
RMSE

# ============
# [1] 4.88772
# ============


# 多重共线性检验
# install.packages("car")
library(car)
vif(fit)

# =============================
#       AT        V       AP
# 3.888380 3.482090 1.348401
# =============================



# 异常的检验
# 高杠杆值点（帽子矩阵）
leverage <- hatvalues(fit)

# dffits值
Dffits <- dffits(fit)

# 学生化残差
resid_stu <- Dffits/sqrt(leverage/(1-leverage))

# cook距离
cook <- cooks.distance(fit)

# covratio值
Covratio <- covratio(fit)
head(Covratio)

# 将上面的几种异常值检验统计量与原始数据集合并
ccpp_outliers <- cbind(ccpp, data.frame(leverage, Dffits, resid_stu, cook, Covratio))
head(ccpp_outliers)

# ================================================================================================
#      AT     V      AP    RH     PE     leverage       Dffits  resid_stu         cook Covratio
# 1 14.96 41.76 1024.07 73.17 463.26 0.0005490939 -0.022075005 -0.9417990 1.218279e-04 1.000597
# 2 25.18 62.96 1020.04 59.08 444.37 0.0004868418  0.003667571  0.1661800 3.363110e-06 1.000894
# 3  5.11 39.40 1012.16 92.14 488.56 0.0007871327  0.032756446  1.1670832 2.682360e-04 1.000636
# 4 20.86 57.32 1010.24 76.64 446.48 0.0001371331 -0.010641243 -0.9086391 2.830953e-05 1.000210
# 5 10.82 37.50 1009.23 96.62 473.90 0.0005139237  0.001008418  0.0444713 2.542535e-07 1.000932
# 6 26.27 59.44 1012.23 58.77 443.67 0.0002427063  0.006290653  0.4037407 9.893944e-06 1.000593
# ================================================================================================

# 计算异常值数量的比例
outliers_ratio = sum(abs(ccpp_outliers$resid_stu)>2)/nrow(ccpp_outliers)
outliers_ratio

# ================
# [1] 0.03710284
# ================

# 删除异常值
ccpp_outliers = ccpp_outliers[abs(ccpp_outliers$resid_stu)<=2,]



# 重新建模
fit2 = lm(PE ~ AT + V + AP, data = ccpp_outliers)
summary(fit2)

# =================================================================
# Call:
# lm(formula = PE ~ AT + V + AP, data = ccpp_outliers)
#
# Residuals:
#      Min       1Q   Median       3Q      Max
# -10.0800  -3.2521  -0.0647   3.1998  10.3041
#
# Coefficients:
#               Estimate Std. Error t value Pr(>|t|)
# (Intercept) 349.825814   8.856741   39.50   <2e-16 ***
# AT           -1.671860   0.011852 -141.06   <2e-16 ***
# V            -0.328487   0.006499  -50.55   <2e-16 ***
# AP            0.153113   0.008676   17.65   <2e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# Residual standard error: 4.265 on 9209 degrees of freedom
# Multiple R-squared:  0.9368,	Adjusted R-squared:  0.9368
# F-statistic: 4.55e+04 on 3 and 9209 DF,  p-value: < 2.2e-16
# =================================================================


# 计算模型的RMSE值
RMSE2 = sqrt(mean(fit2$residuals**2))
RMSE2

# ==============
# [1] 4.264442
# ==============


# 正态性检验

# 绘制直方图
hist(x = fit2$residuals, freq = FALSE,
    breaks = 100, main = 'x的直方图',
    ylab = '核密度图', xlab = NULL, col = 'steelblue')

# 添加核密度图
lines(density(fit2$residuals), col = 'red', lty = 1, lwd = 2)

# 添加正态分布图
x <- fit2$residuals[order(fit2$residuals)]
lines(x, dnorm(x, mean(x), sd(x)),
        col = 'blue', lty = 2, lwd = 2.5)

# 添加图例
legend('topright', legend = c('核密度曲线','正态分布曲线'),
        col = c('red','blue'), lty = c(1,2),
        lwd = c(2,2.5), bty = 'n')


# PP图
real_dist <- ppoints(fit2$residuals)
theory_dist <- pnorm(fit2$residuals, mean = mean(fit2$residuals), sd = sd(fit2$residuals))

# 绘图
plot(sort(theory_dist), real_dist, col = 'steelblue', pch = 20, main = 'PP图',
    xlab = '理论正态分布累计概率', ylab = '实际累计概率')

# 添加对角线作为参考线
abline(a = 0, b = 1, col = 'red', lwd = 2)


# QQ图
qqnorm(fit2$residuals, col = 'steelblue', pch = 20, main = 'QQ图',
        xlab = '理论分位数', ylab = '实际分位数')

# 绘制参考线
qqline(fit2$residuals, col = 'red', lwd = 2)


# Shapiro正态性检验

# shapiro <- shapiro.test(fit2$residuals)
# shapiro

# K-S正态性检验
fit2_resi <- fit2$residuals
ks <- ks.test(jitter(fit2_resi), 'pnorm', mean = mean(fit2_resi), sd = sd(fit2_resi))
# jitter  不能有重复值，使用jitter做小扰动,参见：http://www.dataguru.cn/forum.php?mod=viewthread&tid=120859
ks

# =========================================
# 	One-sample Kolmogorov-Smirnov test
#
# data:  jitter(fit2_resi)
# D = 0.030707, p-value = 5.694e-08
# alternative hypothesis: two-sided
# =========================================


# 加载第三方包
# install.packages("lmtest")
# install.packages("lmtest")
library(ggplot2)
library(gridExtra)
library(lmtest)
library(nlme)


# 异方差性检验
# ====== 图示法完成方差齐性的判断 ======
# 标准化误差
std_err <- scale(fit2$residuals)
# 绘图
ggplot(data = NULL, mapping = aes(x = fit2$fitted.values, y = std_err)) +
    geom_point(color = 'steelblue') +
    geom_hline(yintercept = 0, color = 'red', size = 1.5) +  # 水平参考线
    labs(x = '预测值', y = '标准化误差')

# + geom_point(color = 'steelblue') 加号放前面会不生效,放在每句后面


# ====== 统计法完成方差齐性的判断 ======
# Breusch-Pagan
bptest(fit2)

# ==========================================
# 	studentized Breusch-Pagan test
#
# data:  fit2
# BP = 26.583, df = 3, p-value = 7.2e-06
# ==========================================


# 自变量与残差的关系
p1 <- ggplot(data = NULL, mapping = aes(x = ccpp_outliers$AT, y = std_err)) +
  geom_point(color = 'steelblue') +
  geom_hline(yintercept = 0, color = 'red', size = 1.5) + # 水平参考线
  labs(x = 'AT', y = '标准化残差')

p2 <- ggplot(data = NULL, mapping = aes(x = ccpp_outliers$V, y = std_err)) +
  geom_point(color = 'steelblue') +
  geom_hline(yintercept = 0, color = 'red', size = 1.5) + # 水平参考线
  labs(x = 'V', y = '标准化残差')

p3 <- ggplot(data = NULL, mapping = aes(x = ccpp_outliers$AP, y = std_err)) +
  geom_point(color = 'steelblue') +
  geom_hline(yintercept = 0, color = 'red', size = 1.5) + # 水平参考线
  labs(x = 'AP', y = '标准化残差')

p4 <- ggplot(data = NULL, mapping = aes(x = ccpp_outliers$AT**2, y = std_err)) +
  geom_point(color = 'steelblue') +
  geom_hline(yintercept = 0, color = 'red', size = 1.5) + # 水平参考线
  labs(x = 'AT^2', y = '标准化残差')

p5 <- ggplot(data = NULL, mapping = aes(x = ccpp_outliers$V**2, y = std_err)) +
  geom_point(color = 'steelblue') +
  geom_hline(yintercept = 0, color = 'red', size = 1.5) + # 水平参考线
  labs(x = 'V^2', y = '标准化残差')

p6 <- ggplot(data = NULL, mapping = aes(x = ccpp_outliers$AP**2, y = std_err)) +
  geom_point(color = 'steelblue') +
  geom_hline(yintercept = 0, color = 'red', size = 1.5) + # 水平参考线
  labs(x = 'AP^2', y = '标准化残差')

grid.arrange(p1,p2,p3,p4,p5,p6,ncol = 3)




# 三种权重
w1 = 1/abs(fit2$residuals)
w2 = 1/fit2$residuals**2
ccpp_outliers['loge2'] = log(fit2$residuals**2)
model = lm('loge2~AT+V+AP', data = ccpp_outliers)
w3 = 1/(exp(model$fitted.values))

# WLS的应用
fit3 = lm('PE~AT+V+AP', data = ccpp_outliers, weights = w1)
summary(fit3)

# ===================================================================
# Call:
# lm(formula = "PE~AT+V+AP", data = ccpp_outliers, weights = w1)
#
# Weighted Residuals:
#     Min      1Q  Median      3Q     Max
# -3.1865 -1.7927 -0.2135  1.7928  3.2337
#
# Coefficients:
#               Estimate Std. Error t value Pr(>|t|)
# (Intercept) 353.341367   3.327478  106.19   <2e-16 ***
# AT           -1.675571   0.004299 -389.76   <2e-16 ***
# V            -0.329469   0.002257 -145.96   <2e-16 ***
# AP            0.149760   0.003252   46.05   <2e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# Residual standard error: 1.879 on 9209 degrees of freedom
# Multiple R-squared:  0.9904,	Adjusted R-squared:  0.9904
# F-statistic: 3.178e+05 on 3 and 9209 DF,  p-value: < 2.2e-16
# ===================================================================

# 异方差检验
het3 = bptest(fit3)
# 模型AIC值
extractAIC(fit3)

=======================
[1]     4.00 11630.41
=======================

fit4 = lm('PE~AT+V+AP', data = ccpp_outliers, weights = w2)
summary(fit4)

# ===================================================================
# Call:
# lm(formula = "PE~AT+V+AP", data = ccpp_outliers, weights = w2)
#
# Weighted Residuals:
#     Min      1Q  Median      3Q     Max
# -1.2530 -0.9995 -0.9686  1.0005  1.2349
#
# Coefficients:
#               Estimate Std. Error t value Pr(>|t|)
# (Intercept)  3.500e+02  2.557e-01  1368.9   <2e-16 ***
# AT          -1.672e+00  3.461e-04 -4831.7   <2e-16 ***
# V           -3.283e-01  1.970e-04 -1666.5   <2e-16 ***
# AP           1.530e-01  2.462e-04   621.2   <2e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# Residual standard error: 1 on 9209 degrees of freedom
# Multiple R-squared:      1,	Adjusted R-squared:      1
# F-statistic: 7.963e+07 on 3 and 9209 DF,  p-value: < 2.2e-16
# ===================================================================

het4 = bptest(fit4)
extractAIC(fit4)

# =======================
# [1] 4.000000 4.779312
# =======================

fit5 = lm('PE~AT+V+AP', data = ccpp_outliers, weights = w3)
summary(fit5)

# ===================================================================
# Call:
# lm(formula = "PE~AT+V+AP", data = ccpp_outliers, weights = w3)
#
# Weighted Residuals:
#     Min      1Q  Median      3Q     Max
# -4.3483 -1.3178 -0.0204  1.3042  4.1407
#
# Coefficients:
#               Estimate Std. Error t value Pr(>|t|)
# (Intercept) 359.739655   8.790432   40.92   <2e-16 ***
# AT           -1.685884   0.011861 -142.14   <2e-16 ***
# V            -0.327177   0.006544  -50.00   <2e-16 ***
# AP            0.143529   0.008609   16.67   <2e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# Residual standard error: 1.742 on 9209 degrees of freedom
# Multiple R-squared:  0.9378,	Adjusted R-squared:  0.9378
# F-statistic: 4.632e+04 on 3 and 9209 DF,  p-value: < 2.2e-16
# ===================================================================

het5 = bptest(fit5)
extractAIC(fit5)

# =======================
# [1]     4.00 10231.81
# =======================

summary(fit2)

# ===================================================================
# Call:
# lm(formula = PE ~ AT + V + AP, data = ccpp_outliers)
#
# Residuals:
#      Min       1Q   Median       3Q      Max
# -10.0800  -3.2521  -0.0647   3.1998  10.3041
#
# Coefficients:
#               Estimate Std. Error t value Pr(>|t|)
# (Intercept) 349.825814   8.856741   39.50   <2e-16 ***
# AT           -1.671860   0.011852 -141.06   <2e-16 ***
# V            -0.328487   0.006499  -50.55   <2e-16 ***
# AP            0.153113   0.008676   17.65   <2e-16 ***
# ---
# Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
# Residual standard error: 4.265 on 9209 degrees of freedom
# Multiple R-squared:  0.9368,	Adjusted R-squared:  0.9368
# F-statistic: 4.55e+04 on 3 and 9209 DF,  p-value: < 2.2e-16
# ===================================================================

het2 = bptest(fit2)
extractAIC(fit2)

========================
[1]     4.00 26731.44
========================

print(paste0('模型fit2的AIC：',round(extractAIC(fit2)[2],2)))
print(paste0('模型fit3的AIC：',round(extractAIC(fit3)[2],2)))
print(paste0('模型fit4的AIC：',round(extractAIC(fit4)[2],2)))
print(paste0('模型fit5的AIC：',round(extractAIC(fit5)[2],2)))

# ==================================
# [1] "模型fit2的AIC：26731.44"
# [1] "模型fit3的AIC：11630.41"
# [1] "模型fit4的AIC：4.78"
# [1] "模型fit5的AIC：10231.81"
# ==================================



# 残差独立性检验library(car)
durbinWatsonTest(fit4)

ggplot(data = NULL, mapping = aes(fit4$fitted.values, ccpp_outliers$PE)) +
  geom_point() +
  geom_smooth(method = 'lm') +
  labs(x = '预测值', y = '实际值')





1
