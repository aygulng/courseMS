from math import sqrt

import pandas

read=pandas.read_csv('D:/PycharmProjects/courseMS/task3/r3z1.csv')

x = read['X']

#объем выборки
n=len(x)

def average(x):
    return sum(x) / len(x)
print('среднее:', average(x))

#смещенная дисперсия
def nesmesh_dispersion(n):
    x=average(n)
    f=[(xi - x)** 2 for xi in n]
    return sum(f) / (len(n)-1)
print('смещенная дисперсия:', nesmesh_dispersion(x))

#cтандартное отклонение
def standard_deviation(n):
    return sqrt(nesmesh_dispersion(n))
print('cтандартное отклонение:',standard_deviation(x))

from scipy import integrate
def f(x):
    o=3
    xo=1
    return o*xo**(o)*x**(-o-1)
o=3
xo=1
v, err = integrate.quad(f, xo, 100)
print(v)

matozh = sum(x) / len(x)
print(f'Мат ожидание: {matozh}')

disp = sum([(value - matozh) ** 2 for value in x]) / (len(x))
print(f'Дисперсия: {disp}')

sredquadotkl = disp ** 0.5
print(f'Среднеквадратическое отклонение: {sredquadotkl}')

# a = matozh - ((3 ** 0.5) * sredquadotkl)
# print(f'a: {a}')
# h = 2 * (3 ** 0.5) * sredquadotkl
# print(f'h: {h}')

