import math

import matplotlib.pyplot as plt
import numpy as np
import pandas
from scipy.stats import expon
import scipy

read = pandas.read_csv('D:/PycharmProjects/courseMS/task2/r2z2.csv')
data=read['X']

# Вариант Z5 (Критерий согласия Колмогорова):
# К заданию прилагается одна выборка и дополнительные параметры:
#требуемый уровень значимости критерия α и вид гипотезы H0 .
# α = 0.05
# H0 : X ∼ E(λ = 2)

# график ЭФР с наложением графика функции
# распределения предполагаемого распределения
data_sort=sorted(data)
x = np.array(data_sort, dtype=float)
x = sorted(list(np.concatenate((x, data))))
print(len(data))
F=[]
for i in x:
    F.append((len(data[data < i-0.001]) / len(data)))
# F=[len(data[data<y])/len(data) for y in x]

lam=2
expF = scipy.stats.expon.cdf(x, scale=1./lam)
plt.plot(x, expF)
plt.plot(x, F)
plt.legend()
plt.show()

alpha=0.05

Dn=max(abs(F-expF))
print('Максимальное расхождение проверяемых функций: ',Dn)

C=np.sqrt(-0.5*np.log(alpha/2))
print('Критическая константа: ',C)

l=np.sqrt(len(data))*Dn
print('Статистика Критерия: ',l)

# p = 0
# for k in range(1,len(data)):
#     p += (-1)**(k-1) * (np.exp(-2*k*k*l*l))
# p = p * 2
# print('',p)

p=1-1+2*(math.exp(-2*l*l))
print(p)

# pp=1.36/math.sqrt(len(data))
# print(pp)

if l <= C:
    print("H0")
else:
    print("H1")

