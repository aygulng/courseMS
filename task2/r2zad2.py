import pandas as pd
from scipy import stats
import seaborn as ss

import matplotlib.pyplot as plt
import collections as c#чтобы выводить значения и их количества в кортежах

viborka = pd.read_csv('D:/PycharmProjects/courseMS/task2/r2z1.csv')


# In[17]:


viborka['R'] = viborka['X'] - viborka['Y']#поэтому уменьшается
ryad = viborka['R'].tolist()
vib_sred = sum(ryad) / len(ryad)
razr = viborka['R'].size

disp_smesh = 0
print(max(ryad), min(ryad), vib_sred)
for i in ryad:
    disp_smesh += (i - vib_sred) ** 2

disp_smesh /= len(ryad)

statistika = vib_sred * (len(ryad) - 1) ** 0.5 / disp_smesh ** 0.5


#значение степень свободы
c_krit = stats.t.ppf(1-0.025, df=len(ryad) - 1)
p_val = stats.t.cdf(statistika, df=len(ryad) - 1)
print('c_krit - ', c_krit)
print('p val  - ', p_val)
print('статистика ', statistika)

'''возьмем за h0 что статистика = 0, а за h1, что она уменьшается, так как X-Y<0
 тогда H1  t<Ckrit
'''
if statistika < c_krit:
    print("принимаем H1 c стат ошибкой 0.0025, значения в выборке увеличиваются")
else:
    print("принимаем H0 c стат ошибкой 0.0025, значения в выборке не увеличиваются")
