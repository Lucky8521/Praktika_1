x=0
y =0
result =True
while result:
        words = [
            'влево',
            'вправо',
            'вниз',
            'вверх', 
            'стоп'
        ]
        a = input("Введите движение персонажа(например: влево вверх вправо вниз): ")
        if a == words[4]:
            break
        try:
            b = float(input("Введите количесво шагов: "))
        except ValueError:
            print('Неверный формат, введите целое или дробное число!')
            continue
        if b < 0:
            print("Введите пожалуйста положительное число!!!")
            continue
        elif a == words[0]:
            x -= b
        elif a == words[1]:      
            x += b
        elif a == words[2]:
            y -= b
        elif a == words[3]:
            y += b
        else:
            print("Вы ввели не коректное слово, введите слово из примера!!!")
            continue
        print("Персонаж находиться на позиции :"+ "(" + str(x) +":" + str(y) +")" )
print("Конечная точка персонажа :"+ "(" + str(x) +":" + str(y) +")")