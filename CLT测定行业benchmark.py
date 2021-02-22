from  numpy import *
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy  as np

#数据
data=pd.read_excel(r'C:\Users\ant.zheng\Desktop\行业二级分类数据0128.xlsx',sheet_name='游戏')
# data=data[data['spend']>=1]
# data=data[data['industry_II_name']=='SLG']
print(data.head())

#抽样分布并测定其均值
def mean_by_n(ls, n):
    for i in range(0, len(ls)-n,100):
        yield ls[i:i+n].mean()

def listmean_by_n(ls, n):
    return list(mean_by_n(ls, n))

#调用CLT
df=listmean_by_n(data['CTR'],100)
print('样本数量:'+str(len(df)))


#正态性检验
# 计算均值
u = np.mean(df)
# 计算标准差
std = np.std(df)  # 计算标准差
print('scipy.stats.kstest统计检验结果：----------------------------------------------------')
results=stats.kstest(df, 'norm', (u, std))
print(results)
print('-----------------------------------------------------------------------------------')

if results[1]>0.05:
    print('本组CTR的均值和标准差分别为:')
    print('均值:'+str(round(np.mean(df),4)),'标准差:'+str(round(np.std(df),4)))
else:
    print('请重新检测！')

#制作正态分布曲线
mu, sigma , num_bins = np.mean(df), np.std(df), 30
x = df
# 正态分布的数据
n, bins, patches = plt.hist(x, num_bins, normed=True, facecolor = 'blue', alpha = 0.5)
plt.show()

