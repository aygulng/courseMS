from math import sqrt
import pandas
import matplotlib.pyplot as plt
import numpy as np


def readX():
    return pandas.read_csv('D:/PycharmProjects/courseMS/task1/r1z1.csv')['X']
x = readX()

# объем выборки
def counter():
    return x.count()
print('объем выборки:', counter())

# минимум
# def minimum(n):
#     return min(n)
print('минимум:', min(x))

# максимум
# def maximum(n):
#     return max(n)
print('максимум:', max(x))

# размах
def delta(n):
    return max(n) - min(n)
print('размах:', delta(x))

# среднее
def average(n):
    return sum(n) / len(n)
print('среднее:', average(x))

#смещенная дисперсия
def smesh_dispersion(n):
    x=average(n)
    f=[(xi - x)** 2 for xi in n]
    return sum(f) / (len(n))
print('смещенная дисперсия:', smesh_dispersion(x))

#несмещенная дисперсия
def nesmesh_dispersion(n):
    x=average(n)
    f=[(xi - x)** 2 for xi in n]
    return sum(f) / (len(n)-1)
print('несмещенная дисперсия:', nesmesh_dispersion(x))

#cтандартное отклонение
def standard_deviation(n):
    return sqrt(nesmesh_dispersion(n))
print('cтандартное отклонение:',standard_deviation(x))

#Медиана — это средний элемент отсортированного набора данных.
def median(n):
    mid = len(n) // 2
    sortedList=sorted(n)
    if len(n) % 2 == 1:
        return sortedList[mid]
    else:
        return (sortedList[mid] + sortedList[mid+1])/2
print('медиана:',median(x))
#выборочнная медиана и обычгая и тд

#асимметрия
def asymmetry(n):
    x = average(n)
    f = [(xi - x) ** 3 for xi in n]
    return sum(f) / ((len(n) * standard_deviation(n) ** 3))
print('асимметрия:',asymmetry(x))

def excess(n):
    x = average(n)
    f = [(xi - x) ** 4 for xi in n]
    return (sum(f)/ ((len(n) * standard_deviation(n) ** 4)))-3
print('excess:',excess(x))

def quartile_1(n):
    sortedList= sorted(n)
    return sortedList[int(len(n) * 0.25)]

def quartile_3(n):
    sortedList = sorted(n)
    return sortedList[int(len(n) * 0.75)]

#интерквартильная широта
def shirota(n):
    return quartile_3(n)-quartile_1(n)
print('интерквартильная широта:',shirota(x))

#гисторамма
def histogram(n):
    # bins = n side означает, что данные разделены на n интервалов.
    # bin_width = 2 * (shirota(x)) * len(x) ** (-task1 / 3)
    # bins = round((x.max() - x.min()) / bin_width)
    #plt.hist(n,len(n)//10)

    plt.hist(n, density=True, bins=8, label="Data")

    plt.legend(loc="upper left")

    plt.title("Гистограмма")
    plt.show()
histogram(x)

def empirical_cdf(n):
    levels = np.linspace(0, 1, len(n) +1)  #
    plt.step(sorted(list(n) + [max(n)]),levels)  # создает пошаговый график, который является определением эмпирического CDF
    plt.show()
empirical_cdf(x)
print(x.mode()[0])
