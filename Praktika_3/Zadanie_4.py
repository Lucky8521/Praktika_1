from math import *
from typing import Counter
from sympy import *
"""Функция znach() для укарачивание кода, запоминаем все 3 ввода в переменную а"""
def znach(value_check, flag_a = False):
    while True:
        try:
            #Объявляем переменную
            a =int(input("Введите перменную " + value_check))
            #Проверка на 0 == 0
            if (flag_a and 
                a == 0):
                print("Переменная а не может равняться 0")
            else:
                return a
        except ValueError:
            print('Неверный формат, введите целое число!')
print ("решаем квадратное уравнение: a*x^2 +b*x + c=0")
j = Symbol('j')
#Вызываем функцию
a = znach('a: ', True)
b = znach('b: ')
c = znach('c: ')
#Ищем дискриминант и корни
discriminant = b ** 2 - 4*a*c
if discriminant > 0:
    x_1= ((-b-sqrt(discriminant))/(2*a))
    x_2= ((-b+sqrt(discriminant))/(2*a))
    print("Два корня: " + "x_1: "+ str(round(x_1, 3)) +"\t"+ "x_2: " + str(round(x_2, 3)))
elif discriminant == 0:
    x_1 = -b/(2*a)
    print("Один корень: " + "x_1: " + str(round(x_1, 3)))
elif discriminant < 0:
    disc =  - discriminant
    kor = sqrt(disc)/(2*a)
    x_1 = -b/(2*a)
    if kor == 1 :
        print ("Корень с отрицательным дискриминантом 1: " + str(x_1) + " + "  + str(j))
        print ("Корень с отрицательным дискриминантом 2: " + str(x_1) + " - "  + str(j))
    else:
        print ("Корень с отрицательным дискриминантом 1: " + str(x_1) + " + " + str(round(kor, 3)) + str(j))
        print ("Корень с отрицательным дискриминантом 2: " + str(x_1) + " - " + str(round(kor, 3)) + str(j))