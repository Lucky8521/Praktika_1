def transform(obraz):
    b = bytes(obraz, 'utf-8')
    return b
def obrattrans(obraz):
    a = (obraz.decode('utf-8'))
    return a
kart = ()
mas_0 = []
mas_1 = []
mas_2 = []
while True:
    a = str(input("Введите надпись, если хотите закончить введите y: "))
    if a == "y":
        kart = tuple(mas_0)
        for i in kart:
            mas_1.append(transform(i))
        print(mas_1)
        for n in mas_1:
            mas_2.append(obrattrans(n))
        print(mas_2)    
        break
    #Добавляем элементы в конец Списка
    mas_0.append(a)
