from math import *
print ("решаем квадратное уравнение: a*x^2 +b*x + c=0")
"""Цикл для поиска дискриминанта"""
while True:
    try:
        a =int(input("Введите перменную a: "))
        break
    except ValueError:
            print('Неверный формат, введите целое число!')
while True:
    try:
        b = int(input("Введите перменную b: "))
        break
    except ValueError:
            print('Неверный формат, введите целое число!')
while True:
    try:
        c = int(input("Введите перменную c: "))
        break
    except ValueError:
            print('Неверный формат, введите целое число!')
discriminant = b ** 2 - 4*a*c
if discriminant > 0:
    x_1= ((-b)-sqrt(discriminant))/(2*a)
    x_2= ((-b)+sqrt(discriminant))/(2*a)
    print("Два корня: " + "x_1: "+ str(round(x_1, 3)) +"\t"+ "x_2: " + str(round(x_2, 3)))
elif discriminant == 0:
    x_1 = -b/(2*a)
    print("Один корень: " + "x_1: " + str(round(x_1, 3)))
elif discriminant < 0:
    print("Корней нет!!")
