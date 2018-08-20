# LinearRegression.py(线性回归诊断)
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

# http://f.dataguru.cn/thread-598486-1-1.html

# 岭回归 和 LASSO回归的理论知识，其实质就是在线性回归的基础上添加了2范数和1范数的惩罚项。
# 这两个模型的关键点是找到一个合理的lambda系数，来平衡模型的方差和偏差，从而得到比较符合
# 实际的回归系数。本期是基于之前讨论的理论部分，采用Python语言和R语言，完成对岭回归和LASSO
# 回归的实践。文中所利用的数据集来自R语言 ISIR包 中的 Hitters数据集，描述的是关于棒球运动员
# 收入的相关信息。

# # # # # # # # # # # # # # # # # # # # # # # #
# 岭回归
# # # # # # # # # # # # # # # # # # # # # # # #

# 原始数据集存在收入的缺失，我们不妨先把这样的观测删除，同时，数据集中含有离散变量，需要将这些
# 变量转换为哑变量后方可建模，故第一步需要对原始数据集进行清洗。

# ===== Python3 =====

# 导入第三方包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# cross_validation(被弃用了)  cross_validation.py:41: DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved.
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.linear_model import Lasso, LassoCV
from sklearn.metrics import mean_squared_error

# 读取数据
df = pd.read_csv('F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/Hitters.csv')
# 哑变量处理（处理离散变量）
dummies = pd.get_dummies(df[['League','Division','NewLeague']])
# 将原始数据集与哑变量数据合并起来
mydf = df.join(dummies)
# 缺失值删除
mydf = mydf.dropna()
# 删除不必要的变量（字符串变量和各哑变量的一个变量）
mydf = mydf.drop(['League','Division','NewLeague','League_N','Division_W','NewLeague'], axis = 1)
# 前5行展示
mydf.head()

'''=============================================================================================================================
   AtBat  Hits  HmRun  Runs  RBI  Walks     ...       Errors  Salary  League_A  Division_E  NewLeague_A  NewLeague_N
1    315    81      7    24   38     39     ...           10   475.0         0           0            0            1
2    479   130     18    66   72     76     ...           14   480.0         1           0            1            0
3    496   141     20    65   78     37     ...            3   500.0         0           1            0            1
4    321    87     10    39   42     30     ...            4    91.5         0           1            0            1
5    594   169      4    74   51     35     ...           25   750.0         1           0            1            0
============================================================================================================================='''


#     上面的数据集清洗完毕，展现的是干净数据的前5行信息，下面要基于这个歌数据集进行建模。
# 建模之前还需要将数据集拆分为两部分，一部分用于建模，另一部分用于模型的测试。

# 将数据集拆分成训练集和测试集
predictors = list(mydf.columns)
predictors.remove('Salary')             # Salay变量为因变量，故需要排除

X_train, X_test, y_train, y_test = train_test_split(mydf[predictors], mydf['Salary'], test_size = 0.2, random_state = 1234)


# 基于可视化，选择lambda参数

# 通过不确定的 alphas值，生成不同的岭回归模型
alphas = 10**np.linspace(-3,3,100)
ridge_cofficients = []

for alpha in alphas:
    ridge = Ridge(alpha = alpha, normalize=True)
    ridge.fit(X_train, y_train)
    ridge_cofficients.append(ridge.coef_)

# 绘制 alpha的对数与回归系数的关系
# 中文乱码的处理和坐标轴负号的处理   KaiTi 楷体、FangSong 仿宋、SimSun 宋体、SimHei 黑体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 设置绘图风格
plt.style.use('ggplot')
plt.plot(alphas, ridge_cofficients)
plt.xscale('log')
plt.axis('tight')
plt.title('alpha系数与岭回归系数的关系')
plt.xlabel('Log Alpha')
plt.ylabel('Coefficients')
plt.show()


# 从图中的结果来看，alpha在10附近，所有的自变量系数基本趋于稳定（但也不能完全确定是这个值）。
# 接下来，我们采用交叉验证（CV）方法确定最佳的lambda值。

# 基于CV选择lambda值

# 为了找到最佳的lambda值，我们采用交叉验证方法

# 岭回归模型的交叉验证
ridge_cv = RidgeCV(alphas = alphas, normalize=True, scoring='neg_mean_squared_error', cv = 10)
# mean_squared_error（被弃用）  Scoring method mean_squared_error was renamed to neg_mean_squared_error in version 0.18 and will be removed in 0.20.
ridge_cv.fit(X_train, y_train)
# 取出最佳的lambda值
ridge_best_alpha = ridge_cv.alpha_
ridge_best_alpha


'''====================
0.010722672220103232
===================='''

# 原文得到lambda值为 10，暂时不懂什么原因
# 得到lambda值在10附近，这里最佳的lambda值为10，下面，我们要基于这个最佳的lambda值进入岭回归模型
# 的创建和模型验证的阶段

# 基于最佳的lambda值建模
ridge = Ridge(alpha = ridge_best_alpha, normalize=True)
ridge.fit(X_train, y_train)
# 岭回归系数
ridge.coef_

# 预测
ridge_predict = ridge.predict(X_test)
# 预测效果验证
RMSE = np.sqrt(mean_squared_error(y_test, ridge_predict))
RMSE

# 原文得到 RMSE值为 319.9，暂时不懂什么原因
'''===================
286.9090006205055
==================='''

# 经过模型验证，得到的RMSE为319.9。接下来，我们利用同样的逻辑，对比一下LASSO回归模型的效果



# # # # # # # # # # # # # # # # # # # # # # # #
# LASSO回归
# # # # # # # # # # # # # # # # # # # # # # # #

# 基于可视化，选择lambda参数

# 通过不确定的alphas值，生成不同的LASSO回归模型
alphas = 10**np.linspace(-3,3,100)
lasso_cofficients = []

for alpha in alphas:
    lasso = Lasso(alpha = alpha, normalize=True, max_iter=10000)
    lasso.fit(X_train, y_train)
    lasso_cofficients.append(lasso.coef_)

# 绘制alpha的对数与回归系数的关系# 中文乱码和坐标轴负号的处理
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 设置绘图风格
plt.style.use('ggplot')
plt.plot(alphas, lasso_cofficients)
plt.xscale('log')
plt.axis('tight')
plt.title('alpha系数与LASSO回归系数的关系')
plt.xlabel('Log Alpha')
plt.ylabel('Cofficients')
plt.show()

# 从图形结果来看，lambda值应该在1附近，此时LASSO回归的系数也基本趋于稳定（但也不能完全确定
# 是这个值）。同样，我们利用CV方法，来寻找最佳的lambda值。

# 基于CV选择lambda值

# LASSO回归模型的交叉验证
lasso_cv = LassoCV(alphas = alphas, normalize=True, cv = 10, max_iter=10000)
lasso_cv.fit(X_train, y_train)
# 取出最佳的lambda值
lasso_best_alpha = lasso_cv.alpha_
lasso_best_alpha

'''=====================
0.23101297000831605
====================='''

# 通过CV方法得到的lambda结果是0.23，这与我们看图得到的1这个值还是有一点差异的。下面，我们就
# 基于交叉验证得到的最佳lambda值重新构造LASSO回归模型。

# 基于最佳的lambda值建模
lasso = Lasso(alpha = lasso_best_alpha, normalize=True, max_iter=10000)
lasso.fit(X_train, y_train)
# 岭回归系数
lasso.coef_

# 预测
lasso_predict = lasso.predict(X_test)
# 预测结果验证
RMSE = np.sqrt(mean_squared_error(y_test, lasso_predict))
RMSE

'''=====================
286.68446874794336
====================='''

#     对 LASSO回归模型进行验证，发现得到RMSE更小，说明 LASSO回归模型的拟合效果更贴近与Hitters
# 数据集的原貌。
#
#     上面的内容是基于Python工具对 岭回归模型和 LASSO回归模型的实战，接下来，我们再利用R
# 语言对上面的过程再作一次复现，希望对R语言感兴趣的朋友能够有帮助。







# # # # # # # # # # # # # # # # # # # # # # # #
# R语言对比
# # # # # # # # # # # # # # # # # # # # # # # #

# 由于上面的逻辑我们已经通过Python进行了一一说明，这里就不再赘述，只给出R语言代码供参考。
library(caret)
# install.packages('glmnet')    安装失败，多安装几次就成功了。。。
library(glmnet)
# install.packages('ISLR')
library(ISLR)

# 哑变量处理
dummies <- dummyVars(~League+Division+NewLeague, data=Hitters)
dummies <- predict(dummies, newdata = Hitters)
# 数据合并
Hitters_dumy <- cbind(Hitters, dummies)

# 删除缺失值
Hitters_dumy <- na.omit(Hitters_dumy)
# 删除不必要的变量
Hitters_dumy <- subset(Hitters_dumy, select = -c(League,Division,NewLeague,League.N,Division.W,NewLeague.N))

================================================================================================
                  AtBat Hits HmRun Runs RBI Walks Years CAtBat CHits CHmRun CRuns CRBI CWalks
-Alan Ashby         315   81     7   24  38    39    14   3449   835     69   321  414    375
-Alvin Davis        479  130    18   66  72    76     3   1624   457     63   224  266    263
-Andre Dawson       496  141    20   65  78    37    11   5628  1575    225   828  838    354
-Andres Galarraga   321   87    10   39  42    30     2    396   101     12    48   46     33
-Alfredo Griffin    594  169     4   74  51    35    11   4408  1133     19   501  336    194
-Al Newman          185   37     1   23   8    21     2    214    42      1    30    9     24
                  PutOuts Assists Errors Salary League.A Division.E NewLeague.A
-Alan Ashby           632      43     10  475.0        0          0           0
-Alvin Davis          880      82     14  480.0        1          0           1
-Andre Dawson         200      11      3  500.0        0          1           0
-Andres Galarraga     805      40      4   91.5        0          1           0
-Alfredo Griffin      282     421     25  750.0        1          0           1
-Al Newman             76     127      7   70.0        0          1           1
================================================================================================

# 岭回归——可视化选lambda

# 构建训练集和测试集
set.seed(1)
index <- sample(1:nrow(Hitters_dumy), size = 0.8*nrow(Hitters_dumy))
train <- Hitters_dumy[index,]
test <- Hitters_dumy[-index,]

# 绘制lambda值与岭回归系数的关系, 17列为 Salary
fit_ridge <- glmnet(x = as.matrix(train[,-17]), y = train[,17], alpha = 0)
plot(fit_ridge, xvar = 'lambda', label = T)


# 岭回归——交叉验证选lambda
# 岭回归的交叉验证，确定最佳的lambda值

fit_ridge_cv <- cv.glmnet(x = as.matrix(train[,-17]), y = train[,17], alpha = 0)
best_lambda_ridge <- fit_ridge_cv$lambda.min
best_lambda_ridge

==============
[1] 36.57596
==============
# 原文显示 30.36601, 将以上三行代码，执行第三遍会得到 30.36601，未知原因


# 岭回归——建模与验证

# 根据最佳lambda构建岭回归模型
fit_ridge <- glmnet(x = as.matrix(train[,-17]), y = train[,17], alpha = 0)
coeff_ridge <- predict(fit_ridge, s = best_lambda_ridge, type = 'coefficients')
coeff_ridge

# 模型评估
pred_ridge <- predict(fit_ridge, s = best_lambda_ridge, newx = as.matrix(test[,-17]))
RMSE <- sqrt(mean((test$Salary-pred_ridge)**2))
RMSE

==============
[1] 270.1666
==============



Lasso——可视化选lambda

# 绘制lambda值与 LASSO回归系数的关系
fit_lasso <- glmnet(x = as.matrix(train[,-17]), y = train[,17], alpha = 1)
plot(fit_lasso, xvar = 'lambda', label = T)


# LASSO——交叉验证选lambda
# LASSO的交叉验证，确定最佳的lambda值
fit_lasso_cv <- cv.glmnet(x = as.matrix(train[,-17]), y = train[,17], alpha = 1)
best_lambda_lasso <- fit_lasso_cv$lambda.min
best_lambda_lasso

=============
[1] 2.64108
=============

# LASSO——建模与验证
# 根据最佳lambda构建LASSO回归模型
fit_lasso <- glmnet(x = as.matrix(train[,-17]), y = train[,17], alpha = 1)
coeff_lasso <- predict(fit_lasso, s = best_lambda_lasso, type = 'coefficients')
coeff_lasso

============================================
20 x 1 sparse Matrix of class "dgCMatrix"
                       1
(Intercept)  75.95127779
AtBat        -1.30078593
Hits          4.42635374
HmRun         0.40960292
Runs          .
RBI           .
Walks         5.73092789
Years       -16.00162847
CAtBat        .
CHits         .
CHmRun        0.47073104
CRuns         0.93128883
CRBI          0.29329828
CWalks       -0.70133854
PutOuts       0.20783780
Assists       0.08534823
Errors       -0.19273277
League.A    -63.83279717
Division.E  144.14188000
NewLeague.A   .
============================================


# 模型评估
pred_lasso <- predict(fit_lasso, s = best_lambda_lasso, newx = as.matrix(test[,-17]))
RMSE <- sqrt(mean((test$Salary-pred_lasso)**2))
RMSE

================
[1] 262.5091
================
