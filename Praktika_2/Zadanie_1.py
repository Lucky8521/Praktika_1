#цикл выполняеться пока значение True
while True:
    try:
        a = float(input('Введите число а: '))
        b = float(input('Введите число b: '))
        # Возращает первое истиное значение!
        if a == float or b == float:
            raise  Exception
        a1 = a + b # Сложение
        print (a1)
        а2 = a - b # вычитание
        print (а2)
        a3 = a * b # умножение
        print (a3)
        if b == 0:
            print ("Делить на 0 не льзя")
        else: 
            a4 = a / b #деление
            print (a4)
        a5 = a ** b # возведение в степерь
        print (a5)
        if b == 0:
            print ("Делить на 0 не льзя")
        else: 
            a6 = a % b # Деление по модулю
            print (a6)
        if b == 0:
            print ("Делить на 0 не льзя")
        else: 
            a7 = a // b
            print (a7)
        break
    #Выдаем ошибку если введено не число!
    except ValueError:
        print('Неверный формат, введите целое или дробное число!')