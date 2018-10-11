# 26-27_LogisticRegression.py(逻辑)
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

#     Logistic模型主要是用来解决二元分类问题，通过构建分类器，计算每一个样本为目标分类的概率，
# 一般而言，我们会将概率值0.5作为分类的阈值，即概率P大于等于0.5时判别为目标分类，否则为另一种
# 分类。

#     下面的数据是基于用户信息（年龄、性别和年收入）来判断其是否发生购买，数据来源于GitHub。
# 接下来，让我们看看Logistic模型是如何完成二分类问题的落地。

# 本次实验会涉及模型的构建、测试集的预测及模型的验证三个方面

# 理解条件概率（学习贝叶斯公式）
# https://www.zybang.com/question/3ebf214029be153ecdf94297727a4caf.html
# P=P(y=1|X)

# # # # # # # # # # # # # # # # # # # # # # # #
# 数据查阅
# # # # # # # # # # # # # # # # # # # # # # # #

# ===== Python3 =====

# 导入第三方包
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
# from sklearn.cross_validation import train_test_split
# DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved.
# Also note that the interface of the new CV iterators are different from that of this module. This module will be removed in 0.20.
from sklearn import metrics
# !pip install ggplot
from ggplot import *
# c:\users\pjarmy\appdata\local\programs\python\python37\lib\site-packages\ggplot\utils.py:81: FutureWarning: pandas.tslib is deprecated and will be removed in a future version.
# You can access Timestamp as pandas.Timestamp
'''
from ggplot import *
加载包报错如下：

......
c:\users\pjarmy\appdata\local\programs\python\python37\lib\site-packages\ggplot\stats\smoothers.py in <module>()
      2                         unicode_literals)
      3 import numpy as np
----> 4 from pandas.lib import Timestamp
      5 import pandas as pd
      6 import statsmodels.api as sm

修改最后一个报错文件的第四行为： from pandas import Timestamp，解决安装包无法加载的问题
参考：http://tieba.baidu.com/p/5779037402
'''


# 读取数据集
purchase = pd.read_csv('E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/Social_Network_Ads.csv')
# 查看数据类型
purchase.dtypes
# 查看各变量的缺失情况
purchase.isnull().sum()

'''
In [15]: purchase.dtypes
Out[15]:
User ID              int64
Gender              object
Age                float64
EstimatedSalary    float64
Purchased            int64
dtype: object

In [14]: purchase.isnull().sum()
Out[14]:
User ID            0
Gender             0
Age                0
EstimatedSalary    0
Purchased          0
dtype: int64
'''

#     从结果可知，除Gender变量，其余均为数值型变量，那么构建入摸变量时，需要对Gender变量
# 创建哑变量；一般在做数据探索时，需要检查各变量是否存在缺失情况（如果缺失需要借助于删除法、
# 替换法、插值法等完成缺失值的处理，具体可以参考文章【如何使用R语言解决可恶的脏数据】见下），
# 很显然上面的结果并没有显示数据中含有缺失值。
# https://mp.weixin.qq.com/s?__biz=MzIxNjA2ODUzNg==&mid=403255306&idx=1&sn=c5550bdabd2af3365bb992c8e6849b36&scene=21#wechat_redirect



# # # # # # # # # # # # # # # # # # # # # # # #
# 变量处理
# # # # # # # # # # # # # # # # # # # # # # # #

# 对Gender变量作哑变量处理
dummy = pd.get_dummies(purchase.Gender)
# 为防止多重共线性，将哑变量中的 Female删除
dummy_drop = dummy.drop('Female', axis = 1)

# 剔除用户ID和Gender变量
purchase = purchase.drop(['User ID', 'Gender'], axis = 1)
# 如果调用Logit类，需要给源数据集添加截距项
purchase['Intercept'] = 1

# 哑变量和元数据集合并
model_data = pd.concat([purchase, dummy_drop], axis = 1)
model_data.head()

'''
    Age  EstimatedSalary  Purchased  Male
0  19.0          19000.0          0     1
1  35.0          20000.0          0     1
2  26.0          43000.0          0     0
3  27.0          57000.0          0     0
4  19.0          76000.0          0     1
'''

#     上面所做的无非是构建哑变量，然后从哑变量中再剔除一个水平变量（这个非常重要，为了防止
# 多重共线性）；同时还有剔除没有意义的变量 User ID 和不再使用的 Gender变量（因为已经拆分
# 为哑变量了）。整理之后的数据集就如图所示，接下来我们要基于这个数据集进行Logistic模型创建。



# # # # # # # # # # # # # # # # # # # # # # # #
# Logistic模型
# # # # # # # # # # # # # # # # # # # # # # # #

# 将 X和 y分开
X = model_data.drop('Purchased', axis = 1)
y = model_data['Purchased']
# 将数据集拆分为训练集和测试集，训练集与测试集的比例为 75%和 25%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# 根据训练集构建 Logistic分类器
logistic = smf.Logit(y_train, X_train).fit()
logistic.summary()

# Optimization terminated successfully.
#          Current function value: 0.371191
#          Iterations 7
# Out[34]:
# <class 'statsmodels.iolib.summary.Summary'>
"""
                           Logit Regression Results
==============================================================================
Dep. Variable:              Purchased   No. Observations:                  300
Model:                          Logit   Df Residuals:                      296
Method:                           MLE   Df Model:                            3
Date:                Wed, 22 Aug 2018   Pseudo R-squ.:                  0.4367
Time:                        16:52:23   Log-Likelihood:                -111.36
converged:                       True   LL-Null:                       -197.69
                                        LLR p-value:                 3.393e-37
===================================================================================
                      coef    std err          z      P>|z|      [0.025      0.975]
-----------------------------------------------------------------------------------
Age                 0.2272      0.029      7.791      0.000       0.170       0.284
EstimatedSalary   3.55e-05   6.08e-06      5.844      0.000    2.36e-05    4.74e-05
Intercept         -12.2640      1.507     -8.137      0.000     -15.218      -9.310
Male                0.2324      0.339      0.687      0.492      -0.431       0.896
===================================================================================
"""

#     经过7次迭代后，模型系数的计算实现收敛，完成了 Logistic分类器的创建。从上图的结果看，
# 除Male这个哑变量不显著（说明性别这个变量并不能构成用户是否购买的因素）外，其余的偏回归系数
# 均为显著。
#
#
# 下面，我们不妨将Male变量剔除，再做一次 Logistic模型。

# 重新构造分类器
logistic2 = smf.logit('Purchased~Age+EstimatedSalary',
                    data = pd.concat([y_train, X_train], axis = 1)).fit()

logistic2.summary()

# Optimization terminated successfully.
#          Current function value: 0.371982
#          Iterations 7
# Out[9]:
<class 'statsmodels.iolib.summary.Summary'>
"""
                           Logit Regression Results
==============================================================================
Dep. Variable:              Purchased   No. Observations:                  300
Model:                          Logit   Df Residuals:                      297
Method:                           MLE   Df Model:                            2
Date:                Thu, 23 Aug 2018   Pseudo R-squ.:                  0.4355
Time:                        11:31:16   Log-Likelihood:                -111.59
converged:                       True   LL-Null:                       -197.69
                                        LLR p-value:                 4.080e-38
===================================================================================
                      coef    std err          z      P>|z|      [0.025      0.975]
-----------------------------------------------------------------------------------
Intercept         -12.0100      1.445     -8.313      0.000     -14.842      -9.178
Age                 0.2245      0.029      7.831      0.000       0.168       0.281
EstimatedSalary  3.518e-05   6.04e-06      5.821      0.000    2.33e-05     4.7e-05
===================================================================================
"""

print(logistic.aic)
print(logistic2.aic)

'''===================
230.7144841992017
229.1889000867539
==================='''

#     很明显，通过变量的剔除，在保证了所有变量显著的情况下，也降低了模型的AIC，说明，Male
# 哑变量的删除是合理的。

# 优势比
np.exp(logistic2.params)

'''==============================
Intercept          0.000006
Age                1.251669
EstimatedSalary    1.000035
dtype: float64
=============================='''

#     接下来，再来看看模型的系数解释（优势比），在其他变量不变的情况下，用户年龄每增加一个
# 单位（岁），用户购买的概率是不购买概率的1.25倍；用户的年收入每增加一个单位（元），用户购买
# 的概率与不购买的概率几乎相等（因为这里只是计年收入增加1元的概率比，如果收入变量压缩10000倍，
# 那这个概率比肯定就会上升了，因为此时收入上升一个单位就是一万元了）。

# 模型的预测与验证

# 根据分类器，在测试集上预测概率
prob = logistic2.predict(exog = X_test.drop('Male', axis = 1))
# 根据概率值，将观测进行分类，不妨以0.5作为阈值
pred = np.where(prob >= 0.5, 1, 0)

# 根据预测值和实际值构建混淆矩阵
cm = metrics.confusion_matrix(y_test, pred, labels=[0,1])
cm
'''==============================
array([[65,  3],
       [ 8, 24]], dtype=int64)
=============================='''

# 计算模型的准确率
accuracy = cm.diagonal().sum()/cm.sum()
accuracy

'''====
0.89
===='''

#     应用分类器对测试数据集进行测试，这里讲概率值设为0.5，如果概率大于等于0.5，则判断用户
# 会购买，否则不会发生购买。通过这个概率值的设定，我们发现模型的准确率还是非常高的（混淆矩阵
# 对角线代表预测正确的量）。可是但看混淆矩阵还不够，因为当书记不平衡是，计算的准确率也同样会
# 高，并不代表模型就会好，所以我们进一步的借助 ROC曲线下的面积来衡量模型是否合理。


# 绘制 ROC曲线
fpr, tpr, _ = metrics.roc_curve(y_test, pred)
df = pd.DataFrame(dict(fpr=fpr, tpr=tpr))

ggplot(df, aes(x='fpr', y='tpr')) +\
    geom_area(alpha=0.5, fill = 'steelblue') +\
    geom_line() +\
    geom_abline(linetype='dashed', color='red') +\
    labs(x = '1-specificity', y = 'Sensityvity', title = 'ROC Curve AUC=%.3f' % metrics.auc(fpr,tpr))

#     由此看出Python也有ggplot2的绘图语法。从上面的 ROC曲线结果可知，AUC的值超过了0.85，
# 这进一步说明模型的预测效果是非常不错的（一般AUC > 0.8就比较好了）


# 下面我们用R语言重现一遍

# 加载第三方包
# install.packages("pROC")
library(pROC)
library(ggplot2)

# 读取数据
purchase <- read.csv(file = file.choose())
purchase$Purchased = factor(purchase$Purchased)

# 数据类型
str(purchase)

==================================================================================================
'data.frame':	400 obs. of  5 variables:
 $ User.ID        : int  15624510 15810944 15668575 15603246 15804002 15728773 15598044 15694829 15600575 15727311 ...
 $ Gender         : Factor w/ 2 levels "Female","Male": 2 2 1 1 2 2 1 1 2 1 ...
 $ Age            : num  19 35 26 27 19 27 27 32 25 35 ...
 $ EstimatedSalary: num  19000 20000 43000 57000 76000 58000 84000 150000 33000 65000 ...
 $ Purchased      : Factor w/ 2 levels "0","1": 1 1 1 1 1 1 1 2 1 1 ...
==================================================================================================

# 各变量缺失情况
sapply(purchase, function(x) sum(is.na(x)))

===================================================================================
        User.ID          Gender             Age EstimatedSalary       Purchased
              0               0               0               0               0
===================================================================================

# 数据集拆分为训练集和测试集
set.seed(0)
idx = sample(1:nrow(purchase), size = 0.75*nrow(purchase))
train = purchase[idx,]
test = purchase[-idx,]

# 构建 Logistic模型
logit = glm(Purchased ~ ., data = train[,-1], family = binomial(link = 'logit'))
summary(logit)

=============================================================================
Call:
glm(formula = Purchased ~ ., family = binomial(link = "logit"),
    data = train[, -1])

Deviance Residuals:
    Min       1Q   Median       3Q      Max
-2.9598  -0.5218  -0.1577   0.3925   1.8627

Coefficients:
                  Estimate Std. Error z value Pr(>|z|)
(Intercept)     -1.296e+01  1.589e+00  -8.158 3.40e-16 ***
GenderMale       2.847e-01  3.568e-01   0.798    0.425
Age              2.433e-01  3.096e-02   7.857 3.93e-15 ***
EstimatedSalary  3.589e-05  6.412e-06   5.598 2.17e-08 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 389.69  on 299  degrees of freedom
Residual deviance: 204.28  on 296  degrees of freedom
AIC: 212.28

Number of Fisher Scoring iterations: 6
=============================================================================

# 删除性别这个变量
train2 = purchase[idx, -c(1,2)]
test2 = purchase[-idx, -c(1,2)]

# 重新构建 Logistic模型
logit2 = glm(Purchased ~ ., data = train2, family = binomial(link = "logit"))
summary(logit2)

=============================================================================
Call:
glm(formula = Purchased ~ ., family = binomial(link = "logit"),
    data = train2)

Deviance Residuals:
    Min       1Q   Median       3Q      Max
-2.9874  -0.5312  -0.1623   0.3891   1.9180

Coefficients:
                  Estimate Std. Error z value Pr(>|z|)
(Intercept)     -1.264e+01  1.516e+00  -8.339  < 2e-16 ***
Age              2.401e-01  3.047e-02   7.880 3.28e-15 ***
EstimatedSalary  3.524e-05  6.334e-06   5.564 2.64e-08 ***
---
Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 389.69  on 299  degrees of freedom
Residual deviance: 204.92  on 297  degrees of freedom
AIC: 210.92

Number of Fisher Scoring iterations: 6
=============================================================================


# 预测
prob = predict(logit2, newdata = test2)
pred = factor(ifelse(prob <= 0.5, 1, 0), levels = c(0,1), ordered = TRUE)

# 混淆矩阵
Freq = table(test$Purchased, pred)
# 准确率
sum(diag(Freq))/sum(Freq)

======
0.18
======


# 绘制 ROC曲线
ROC = roc(factor(test2$Purchased, levels=c(0,1), ordered = TRUE), pred)
df = data.frame(x = 1-ROC$specificities, y = ROC$sensitivities)

ggplot(df, aes(x = x, y = y)) +
    geom_area(alpha=0.5, fill = 'steelblue') +
    geom_line() +
    geom_abline(linetype='dashed', color='red') +
    labs(x = '1-specificity', y = 'Sensityvity',
        title = paste0('ROC Curve AUC=', round(ROC$auc, 3))) +
    theme(plot.title = element_text(hjust = 0.5, face = 'bold'))
