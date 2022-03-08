from math import inf
import numpy as np
from scipy import stats
import pandas as pd

df1=pd.read_csv('D:/PycharmProjects/courseMS/task4/r4z1.csv')

#(Z14: Проверить гипотезу независимости признаков по критерию сопряженности хи-квадрат)

alf = 0.025
r = 6
s = 5
X1 = 118.05
Xr = 126.05
Y1 = 81.05
Ys = 87.05
print(len(df1)) #100


def calc_n_i_j(i,j):          #метод, который проверяет попадает ли сл.вел. в интервал
    x1 = x_split[i-1]
    x2 = x_split[i]
    y1 = y_split[j-1]
    y2 = y_split[j]
    return df1[(df1['X']<x2) & (df1['X']>x1) & (df1['Y']<y2)  & (df1['Y']>y1)]

n = len(df1)
x_split = [-inf, 118.05, 119.65, 121.25, 122.85, 124.45, 126.05, inf]
y_split = [-inf, 81.05, 82.55, 84.05, 85.55, 87.05, inf]

n_con = np.array([[len(calc_n_i_j(i, j)) for j in range(1, s+2)] for i in range(1, r+2)])   #создаём массив из сл.вел попадающих в интервалы

nX = np.array([sum(s) for s in n_con])

nInv = n_con.transpose()
nY = np.array([sum(s) for s in nInv])
n_con = np.vstack([n_con, nY]) #Функция vstack() соединяет массивы по вертикали

nX = np.append(nX, len(df1['X']))

n_df_con = pd.DataFrame(n_con, columns=['Y1', 'Y2', 'Y3', 'Y4','Y5','Y6'],
                        index=['X1', 'X2', 'X3', 'X4', 'X5','X6','X7','nY'])
n_df_con['nX'] = nX

#статистика критерия сопряжённости хи-квадрат
T=0
for i in range(r+1):
    for m in range(s+1):
        T += ((n*n_con[i][m] - nX[i]*nY[m])**2) / (n*nX[i]*nY[m])  #статистика
print(n_df_con)
print('Статистика T = ',T)

#распределение хи-квадрат Fchisq(t | ν) с ν = (r − 1)(s − 1) степенями свободы
crit_const = stats.chi2.ppf(1-alf,(r)*(s))
print('crit_const = ',crit_const)

#p-значение критерия приближённо вычисляется по формуле p ≈ 1 − Fchisq(T | ν).
p_value = 1 - stats.chi2.cdf(T, (r)*(s))
print('Критический уровень значимости (p-value) = ',p_value)

#Признаки следует признать независимыми, если p > α
print('Уровень значимости = ',alf)
if p_value > alf:
    print("H0 принимается")
else:
    print("H0 отклоняется")