import math
import pandas
from scipy import stats

read=pandas.read_csv('D:/PycharmProjects/courseMS/task2/r2z1.csv')

x = read['X']
y = read['Y']

# объем выборки
def counter(data):
    return data.count()

# среднее
def average(data):
    return sum(data) / len(data)

# несмещенная дисперсия
def nesmesh_dispersion(data):
    x = average(data)
    f = [(xi - x) ** 2 for xi in data]
    return sum(f) / (len(data) )

# # cтандартное отклонение
def standard_deviation(data):
    return math.sqrt(nesmesh_dispersion(data))

print('среднее x:',average(x))
print('среднее y:',average(y))

u = abs(x - y)
print('объем выборки x-y:', len(u))
print('среднее x-y:',average(u))

# Вычислим эмпирическое значение t-критерия Стьюдента используя формулу:
def st(u):
    dis = nesmesh_dispersion(u)
    mo=0
    t = (average(u)-mo) * math.sqrt(len(u) - 1) / math.sqrt(dis)
    return t
print('Статистика одновыборочного критерия Стьюдента равна: ',st(u))

# Вычислим число степеней свободы t-критерия Стьюдента для одной выборки: df=n-1
df = len(u) - 1
a=0.05 #уровень значимости
# Fstud(n) — распределение Стьюдента c n степенями свободы.

def crit_const(alpha, df):
    return stats.t.ppf(1-(alpha), df)

print('Критическая константа: ',crit_const(a,df))

def p_value(data, df):
    return 1-stats.t.cdf((st(data)), df)
print('P-значение: ',p_value(u,df))


if (st(u)) > crit_const(a,df):
    print("H1")
else:
    print("H0")


# правосторон критическую область
# A = {x(n): T > Cкрит}
# Альтернативная гипотеза:
# Если tкрит < tстат — нулевая гипотеза отвергается, где
# t крит — крит конст Стьюдента (наблюдаемое значение критерия)
# tстат. — Эмпирическое значение критерия
# Если tкрит > tстат — нет оснований отвергнуть нулевую гипотезу.


# Н0 : m(z)<0 так как z=x-y,m(x)<m(y).
# Вот и получается, что Н1: m(z)>=0 .
# Смотрю по этой табличке, и беру T>Скр