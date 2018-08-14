# LinearRegression.py(线性回归)
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/


# 从有监督、无监督和半监督的角度来看，回归其实是有监督的算法模型之一
# 反映的是根据某些已知变量（解释变量和自变量）去预测某个未知变量（被解释变量或因变量）
# 例如：过敏生产总值，预测人口失业率、根据房屋的面积、朝向、交通状况等信息，预测房价
    # 根据田地的面积、施肥状况、稻谷的品种、预测粮食产量等

# 对于类似数值型的因变量预测，我们就可以借助于回归来完成
# 关于回归有很多种类，如多元线性回归、岭回归、Lasso回归等


# 多元线性回归
# ************************************************************



# 线性回归模型的创建
# ************************************************************
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 线性回归模型的前提假设

# 由于线性回归模型的偏回归系数通过最小二乘法（OLS）实现，关于最小二乘法的使用时有一些前提假设的

# 自变量与因变量之间存在线性关系
# 自变量之间不存在多重共线性
# 回归模型的残差服从正态分布
# 回归模型的残差满足方差齐性（即方差为某个固定值）
# 回归模型的残差之间相互独立


# 线性回归模型对异常值是非常敏感的，模型的预测结果非常容易受到异常值的影响
# 所有我们还需要对原始数据进行异常点的识别和处理
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# 案例分享

# 销售额与广告渠道的关系

# 如果市场运营部门给了你一份数据，数据包含了不同广告渠道的成本及对应的产品销售量。现在的问题是：

# 哪些渠道的广告真正影响了销售量？
# 根据已知渠道的预算，如何实现销售量的预测？
# 模型预测的好坏，该如何评估？


# 利用Python建模

# 哪些渠道的广告真正影响了销售量？对于这个问题的回答，其实就是在构建多元线性回归模型后，
# 需要对偏回归系数进行显著性检验，把那些最显著的变量保留下来，即可以认为这些变量对销售量
# 是存在影响的。关于线性回归模型的落地，我们这里推荐使用 statsmodels模块，因为该模块相比于sklearn，
# 可以得到更多关于模型的消息信息

# ======= Python3 + Jupyter =======

# !pip install statsmodels
# 导入所需的第三方包
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# 读取外部数据
sales = pd.read_csv('F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/Advertising.csv')
# 查看数据的前5行
sales.head()
# 数据集中各变量的描述性统计分析
sales.describe()


=========================================================
      TV  radio  newspaper  sales
0  230.1   37.8       69.2   22.1
1   44.5   39.3       45.1   10.4
2   17.2   45.9       69.3    9.3
3  151.5   41.3       58.5   18.5
4  180.8   10.8       58.4   12.9

               TV       radio   newspaper       sales
count  200.000000  200.000000  200.000000  200.000000
mean   147.042500   23.264000   30.554000   14.022500
std     85.854236   14.846809   21.778621    5.217457
min      0.700000    0.000000    0.300000    1.600000
25%     74.375000    9.975000   12.750000   10.375000
50%    149.750000   22.900000   25.750000   12.900000
75%    218.825000   36.525000   45.100000   17.400000
max    296.400000   49.600000  114.000000   27.000000
=========================================================

# 数值变量的基本统计值，总数、均值、标准差、最小值、上四分位数、中位数、下四分位数、最大值

# 接下来需要根据读取的数据构造回归模型，在建模之前，一般需要将数据集拆分成训练集（用于建模）
# 和测试集（用于模型的评估）两个部分。

# 抽样--构造训练集和测试集
Train, Test = train_test_split(sales, train_size = 0.8, random_state=1234)

# 建模
fit = smf.ols('sales~TV+radio+newspaper', data = Train).fit()
# 模型概率反馈
fit.summary()

====================================================================================================
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results
==============================================================================
Dep. Variable:                  sales   R-squared:                       0.894
Model:                            OLS   Adj. R-squared:                  0.892
Method:                 Least Squares   F-statistic:                     437.8
Date:                Tue, 14 Aug 2018   Prob (F-statistic):           1.01e-75
Time:                        13:36:57   Log-Likelihood:                -308.29
No. Observations:                 160   AIC:                             624.6
Df Residuals:                     156   BIC:                             636.9
Df Model:                           3
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      2.8497      0.365      7.803      0.000       2.128       3.571
TV             0.0456      0.002     28.648      0.000       0.042       0.049
radio          0.1893      0.009     20.024      0.000       0.171       0.208
newspaper      0.0024      0.007      0.355      0.723      -0.011       0.016
==============================================================================
Omnibus:                       53.472   Durbin-Watson:                   2.153
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              147.411
Skew:                          -1.353   Prob(JB):                     9.77e-33
Kurtosis:                       6.846   Cond. No.                         472.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""
====================================================================================================

# 通过模型反馈的结果我们可知，模型是通过显著性检验的，即 F统计量（ F-statistic）
# 所对应的P值（ Prob (F-statistic)）是远远小于 0.05这个阈值的，
# 说明需要拒绝原假设（即认为模型的所有回归系数都不全为 0）

# 模型的显著性通过检验的话，并不代表每一个自变量对因变量都是重要的
# 所以还需要进行偏回归系数的显著性检验，通过上面的检验结果显示，除变量newspaper对应的P值超过0.05，
# 其余变量都低于这个阈值，说明newspaper这个广告渠道并没有影响到销售量的变动，故需要将其从模型中剔除。



# 重建模型
fit2 = smf.ols('sales~TV+radio', data = Train.drop('newspaper', axis = 1)).fit()
# 模型信息反馈
fit2.summary()

====================================================================================================
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results
==============================================================================
Dep. Variable:                  sales   R-squared:                       0.894
Model:                            OLS   Adj. R-squared:                  0.892
Method:                 Least Squares   F-statistic:                     660.3
Date:                Tue, 14 Aug 2018   Prob (F-statistic):           3.69e-77
Time:                        14:22:29   Log-Likelihood:                -308.36
No. Observations:                 160   AIC:                             622.7
Df Residuals:                     157   BIC:                             631.9
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      2.9004      0.335      8.652      0.000       2.238       3.563
TV             0.0456      0.002     28.751      0.000       0.042       0.049
radio          0.1904      0.009     21.435      0.000       0.173       0.208
==============================================================================
Omnibus:                       54.901   Durbin-Watson:                   2.157
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              156.962
Skew:                          -1.375   Prob(JB):                     8.24e-35
Kurtosis:                       6.998   Cond. No.                         429.
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
"""
====================================================================================================

# 通过第二次建模（模型中剔除了newspaper这个变量），结果非常明朗
# 一方面模型通过了显著性检验，另一方面，所有的变量也通过了显著性检验。
# 问题来了，剔除newspaper这个变量后，模型效果确实变好了吗？
#
# 验证一个模型好不好，只需要将预测值和真实值做一个对比即可
# 如果模型优秀，那预测出来的结果应该会更接近于现实数据。
#



# 下面，我们基于 fit 和 fit2 这两个模型，分别在Test数据集上做预测：

# 第一个模型的预测结果
pred = fit.predict(exog = Test)
# 第二个模型的预测结果
pred2 = fit2.predict(exog = Test.drop('newspaper', axis = 1))

# 模型效果对比
RMSE = np.sqrt(mean_squared_error(Test.sales, pred))
RMSE2 = np.sqrt(mean_squared_error(Test.sales, pred2))
# np.sqrt()     求平方根

print('第一个模型的预测结果：RMSE=%.4f\n' %RMSE)
print('第二个模型的预测结果：RMSE=%.4f\n' %RMSE2)

===================================
第一个模型的预测结果：RMSE=1.7047

第二个模型的预测结果：RMSE=1.6956
===================================

# 对于连续变量预测效果的好坏，我们可以记住RMSE（均方根误差），即真实值与预测值的均方根，来衡量。

# 区分于标准差（真实值vs均值）请见：https://blog.csdn.net/Leyvi_Hsing/article/details/54022612
# MSE(mean squared error 均方误差)  RMSE(root mean squared error 均方根误差，也称标准误差)
# 标准差是用来衡量一组数自身的离散程度，而均方根误差是用来衡量观测值同真值之间的偏差(百度百科)
# variance/deviation Var  方差 D(X)     Standard Deviation  标准差

# 如果这个值越小，就说明模型越优秀，即预测出来的值会越接近于真实值。可以得出模型2更符合实际。




# 最后，我们再利用可视化的方法来刻画真实的观测点与拟合线之间的关系。

# 真实值与预测值的关系
# 设置绘图风格
plt.style.use('ggplot')
# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# 散点图
plt.scatter(Test.sales, pred, label = '观测点')
# 回归线
plt.plot([Test.sales.min(), Test.sales.max()], [pred.min(), pred.max()], 'r--', lw=2, label = '拟合线')

# 添加 x轴标签和标题
plt.title('真实值vs.预测值')
plt.xlabel('真实值')
plt.ylabel('预测值')

# 设置横纵坐标刻度范围
plt.xlim(0,30)
plt.ylim(0,30)

# 去除图形顶部边界和右边界的刻度
plt.tick_params(top=False, right=False)
# 添加图例
plt.legend(loc = 'upper left')
# 图形展现
plt.show()



# ***************************************
# R
# ***************************************

# 读取数据
sales <- read.csv('F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/Advertising.csv')
# 数据的描述性统计
summary(sales)

===================================================================
       TV             radio          newspaper          sales
 Min.   :  0.70   Min.   : 0.000   Min.   :  0.30   Min.   : 1.60
 1st Qu.: 74.38   1st Qu.: 9.975   1st Qu.: 12.75   1st Qu.:10.38
 Median :149.75   Median :22.900   Median : 25.75   Median :12.90
 Mean   :147.04   Mean   :23.264   Mean   : 30.55   Mean   :14.02
 3rd Qu.:218.82   3rd Qu.:36.525   3rd Qu.: 45.10   3rd Qu.:17.40
 Max.   :296.40   Max.   :49.600   Max.   :114.00   Max.   :27.00
===================================================================

# 抽样
set.seed(1234)
index <- sample(1:nrow(sales), size = 0.8*nrow(sales))

train <- sales[index,]
test <- sales[-index,]

# 建模
fit <- lm(sales ~ ., data = train)
# 模型概览信息
summary(fit)

==================================================================
Call:
lm(formula = sales ~ ., data = train)

Residuals:
    Min      1Q  Median      3Q     Max
-8.5904 -0.7857  0.2158  1.2158  3.0468

Coefficients:
             Estimate Std. Error t value Pr(>|t|)
(Intercept)  2.735728   0.377077   7.255 1.77e-11 ***
TV           0.047222   0.001585  29.796  < 2e-16 ***
radio        0.188183   0.009860  19.085  < 2e-16 ***
newspaper   -0.003496   0.006740  -0.519    0.605
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.706 on 156 degrees of freedom
Multiple R-squared:  0.8924,	Adjusted R-squared:  0.8904
F-statistic: 431.4 on 3 and 156 DF,  p-value: < 2.2e-16
==================================================================


# 模型修正
fit2 <- lm(sales ~ TV + radio, data = train)
summary(fit2)

==================================================================
Call:
lm(formula = sales ~ TV + radio, data = train)

Residuals:
    Min      1Q  Median      3Q     Max
-8.4793 -0.8428  0.2505  1.2200  3.0058

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept) 2.662262   0.348650   7.636 2.06e-12 ***
TV          0.047282   0.001577  29.983  < 2e-16 ***
radio       0.186464   0.009265  20.125  < 2e-16 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Residual standard error: 1.702 on 157 degrees of freedom
Multiple R-squared:  0.8922,	Adjusted R-squared:  0.8909
F-statistic:   650 on 2 and 157 DF,  p-value: < 2.2e-16
==================================================================


# 第一个模型预测
vars <- c('TV', 'radio', 'newspaper')
pred <- predict(fit, newdata = test[, vars])

# 第二个模型预测
vars2 <- c('TV', 'radio')
pred2 <- predict(fit2, newdata = test[, vars2])

# 预测效果评估RMSE
RMSE <- function(x,y){
    sqrt(mean((x-y)^2))
}

RMSE1 <- RMSE(test$sales, pred)
RMSE2 <- RMSE(test$sales, pred2)

RMSE1;RMSE2

================
[1] 1.636898
[1] 1.630294
================




# 预测值与实际值对比
plot(test$sales, pred2, type = 'p', pch = 20, col = 'steelblue',
    xlab = '真实值', ylab = '预测值', main = '真实值vs.预测值')
# 设置横纵坐标范围
# xlim=c(0,30), ylim=c(0,30),

# 添加拟合线
lines(x = c(min(test$sales),max(test$sales)),
    y = c(min(pred2), max(pred2)),
    lty=2, col = 'red', lwd = 2)
