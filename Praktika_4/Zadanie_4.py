from typing import *
list_del = []
close = True
i =0
m = 0
prov_peregryz = 0
pro_ves = 40
invent = dict()
while close:
    for k in invent:
        m = 0
        print("Предмет: " + invent[k]['name'] + "\tВес:" + str(invent[k]['ves']))
        if m > 0:
            print("\n")
        m += 1
    print("Текущий вес инвенторя: " + str(prov_peregryz))
    print("Максимальный вес инвенторя: " + str(pro_ves))
    name = input("Введите название предмета: ")
    while True:
        try:
            ves = float(input("Введите вес предмета: "))
            break
        except ValueError:
            print("Введите число!!")
    for q in invent:
        if invent[q]['name'] == name and invent[q]['ves'] == ves:
            print("Такой предмет уже есть")
            break
    else:  
        #invent.update(isName=ves)
        if  prov_peregryz + ves <= pro_ves:
            invent[i] = {'id': 100+i, 'name':name,'ves':ves}
            i +=1
            prov_peregryz += ves
        else: 
            print("Перегруз!!")
            continue
        #print(prov_peregryz)
        # invent[i] = {'id': 100+i, 'name':name,'ves':ves}
        # i +=1
        #print(invent)
        delet = input("Хотите ли вы удалить предмет (Да/Нет): ")
        if delet == 'Да':
            name_del = input("Введите название предмета который хотите удалить: ")
            for del_name in invent:
                if name_del == invent[del_name]['name']:
                    #Добавление элементов в список для удаления!
                    list_del.append(del_name)
            for del_name in list_del:
                invent.pop(del_name)
        if input("Хотите ли вы закончить заполнять инвентарь?(Да/Нет)") == 'Да':
            close = False
        else:
            close = True