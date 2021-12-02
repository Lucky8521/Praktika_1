def kek(fibo):
    if fibo == 0:
        return 0
    if fibo == 1:
        return 1
    else:
        return kek(fibo - 2) + kek(fibo - 1)
#summ = 0
mas = []
while True:
    summ = 0
    #Очищаем Список
    mas.clear()
    try:
        a = int(input("Введите число Фибоначчи: "))
    except ValueError:
        print("Введите число!")
        continue
    for i in range(a):
        summ += kek(i)
        mas.append(kek(i))
    print(mas)
    print("summa: " + str(summ))
    if input("Вы хотите закончить вывод числе? (Да\Нет): ") == "Да":
        break

        