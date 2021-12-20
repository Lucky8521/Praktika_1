from math import *
import time
def test(funk):
    def wrapped():    
       with open("Log.txt", "a", encoding='utf-8') as file:
            tic = time.perf_counter()
            a_1 = funk()
            file.write("\n" + str(a_1))
            toc = time.perf_counter()
            print(f'Вычисление заняло {toc - tic:0.6f} секунд')
            print("Ваш ответ записался в Log.txt!!!")
            time.sleep(5)
    return wrapped 

@test
def uravnenie():
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
        return ("Два корня: " + "x_1: "+ str(round(x_1, 3)) +"\t"+ "x_2: " + str(round(x_2, 3)))
    elif discriminant == 0:
        x_1 = -b/(2*a)
        return ("Один корень: " + "x_1: " + str(round(x_1, 3)))
    elif discriminant < 0:
        return  ("Корней нет!!")
closs= True
while closs:
    uravnenie()
    while True:
        exit = input("Хотите ли вы выйте? (Да/Нет) ")
        if exit == "Да":
            closs = False
            break
        elif exit == "Нет":
            break
        else:
            print("Введите пожалуйста либо Да либо Нет!!!")