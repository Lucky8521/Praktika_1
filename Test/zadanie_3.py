from math import *
def discriminant (a, b ,c):
    discrim = b**2 - 4*a*c
    return discrim
def koren(a,b,c):
    x_1= ((-b)-sqrt((b**2) - (4*a*c)))/(2*a)
    x_2= ((-b)+sqrt(b**2 - 4*a*c))/(2*a)
    return x_1, x_2
def one_koren(a, b):
    x_1 = -b/(2*a)
    return x_1
def zero_koren(a,b,c):
    discrim = b**2 - 4*a*c
    return discrim

print ("решаем квадратное уравнение: a*x^2 +b*x + c=0")
"""Цикл для поиска дискриминанта"""
disc = discriminant(4,5,1)
if disc > 0:
    two_kor = koren(4,5,1)
    print("Два корня: " + str(two_kor))
elif disc == 0:
    x_1 = one_koren(4,5)
    print("Один корень: " + str(x_1))
elif disc < 0:
    print("Корней нет!!")