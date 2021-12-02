def addr(*num):
        sum = 0
        for i in num:
            sum += i
        return sum
#объявляем Картеж
c = ()
mas = []
while True:
    a = input("Введите число, если хотите закончить введите y: ")
    inc_count = str(a)
    #Проверка на ввод только чисел!!
    if not a.isdecimal():
        if inc_count == "y":
            #Добавление в Картеж
            c = tuple(mas)
            print("Ответ " + str(addr(*c)))
            break
        print("Введите число!!")
        continue
    #Добавляем элементы в конец Списка
    mas.append(int(a))