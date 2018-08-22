# LinearRegression.py(线性回归诊断)
# E:/Documents/GitHub/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/
# F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/

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
from sklearn.cross_validation import train_test_split
from sklearn import metrics
# !pip install ggplot
from ggplot import *
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
purchase = pd.read_csv('F:/GitRespository/MyCloud/dataAnalysis/DataAnalysis1480/fromZero/data/Social_Network_Ads.csv')
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
model_data

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
































1
