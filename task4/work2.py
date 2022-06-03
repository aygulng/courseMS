import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

data = pd.read_csv('D:/PycharmProjects/courseMS/task4/r4z2.csv')

x=data['X']
y=data['Y']
n = len(data)
mean_x=np.mean(x)  #среднее
mean_y=np.mean(y)

st_errx= (np.var(x))**0.5 #дисперсия
st_erry= (np.var(y))**0.5

#Выборочная корреляция
ch=0
for i in range(n):
    ch+=(x.loc[i]-mean_x)*(y.loc[i]-mean_y)
cor=ch/(n)/(st_errx * st_erry)

b=cor*st_erry/st_errx

print(cor)

#оценка регрессии
#y=b*x+a
#a=mean_y-b*mean_x
#b=cor*st_erry/st_errx
def ocenka(xx):
    y=b*(xx-mean_x)+mean_y
    return y

#Прогноз Y по X при Х=119
print('Прогноз Y по X при Х=119: ',ocenka(119))


plt.scatter(x, y, marker='.')
plt.plot(x,ocenka(x),"g-")
plt.show()

#Статистика
stat = cor * math.sqrt(n-2)/(1-cor**2)
#Р-значение
p=1-t.cdf(stat,n-2)
print(p)