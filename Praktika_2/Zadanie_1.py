while True:
    try:
        a = float(input('Введите число а: '))
        b = float(input('Введите число b: '))
        """Возращает первое истиное значение!"""
        if (a == float or 
            b == float):
            raise  Exception
        a1 = a+b 
        print ("Сложение:", a1)
        а2 = a-b 
        print ("Вычитание:", а2)
        a3 = a*b 
        print ("Умножение:", a3)
        if b == 0:
            print ("Делить на 0 не льзя")
        else: 
            a4 = a/b #деление
            print ("Деление:", a4)
        a5 = a**b 
        print ("Возведение в степень:", a5)
        if b == 0:
            print ("Делить на 0 не льзя")
        else: 
            a6 = a%b 
            print ("Деление по модулю:", a6)
        if b == 0:
            print ("Делить на 0 не льзя")
        else: 
            a7 = a//b
            print ("Целочисленное деление:", a7)
        break
    except ValueError:
        print('Неверный формат, введите целое или дробное число!')