"""Класс human"""
class human():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.geder = gender
"""Класс student дочерний от human, сдесь обрабатывается сравнения"""
class student(human):
    def __init__(self, name, age, gender, kol_pass_dz):
        super().__init__(name, age, gender)
        self.kol_pass_dz = kol_pass_dz
    def __eq__(self, y):
        return self.kol_pass_dz.__eq__(y.kol_pass_dz)
    def __lt__(self, y):
        return self.kol_pass_dz.__lt__(y.kol_pass_dz)
    def __gt__(self, y):
        return self.kol_pass_dz.__gt__(y.kol_pass_dz)

mas = []
i = 0
invent = {
    1 : {	
        "id": 12423,
        "name":"Алексей",
        "age": 23,
        "gender": "m",
        "kol_pass_dz": 12
    },
    2 : {	
        "id": 12343,
        "name": "Сергей",
        "age": 15,
        "gender": "m",
        "kol_pass_dz": 3
    },
    3 : {	
        "id": 12323,
        "name": "Никита",
        "age": 25,
        "gender": "m",
        "kol_pass_dz": 2
    },
    4 : {	
        "id": 15423,
        "name": "Дмитрий",
        "age": 26,
        "gender": "m",
        "kol_pass_dz": 8
    },	
}
"""Записываем значение словаря в переменные 
присваиваем их объекту и записываем элементы объекта в список """
for q in invent:
    dict_name = invent[q]["name"]
    dict_age = invent[q]["age"]
    dict_gendeder = invent[q]["gender"]
    dict_kol_pass = invent[q]["kol_pass_dz"]
    stud = student(dict_name,dict_age,dict_gendeder,dict_kol_pass)
    mas.append(stud) 
"""Выводим из списка номер и наименование студента"""
for q in invent:
    print( str(q) + " : " + invent[q]["name"])
content = True
while content:
    try:
        number = int(input("Введите номер первого студента: "))
        number_1 =int(input("Введите номер второго студента: "))
    except ValueError:
        print("Введите число пожалуйста!!")
    """Проверяем если нет совпадений по списку, то ошибка с таким номером студентов нет"""
    if number in invent and  number_1 in invent:  
        if number == number_1:
            print("Нельзя брать одного и того же студента!!!")
            continue
        else:
            c = invent[number]["name"]
            c_1 = mas[number - 1]
            e = invent[number_1]["name"]
            e_1 = mas[number_1 - 1]
        if c_1.__eq__(e_1):
            print("Студент " +str(c)+ " cдал cтолько же работ сколько и cтудент " + str(e))
        elif c_1.__gt__(e_1):
            print("Студент " +str(c)+ " сдал больше заданий чем студент " + str(e))
        elif c_1.__lt__(e_1):
            print("Студент " +str(c)+ " сдал меньше заданий чем студент " + str(e))
    else:
        print("Такого номера студента нет!!!!")
        continue
    while True:
        exit = input("Хотители вы выйте из программы?(Да/Нет): ")
        if  exit == "Да":
            content = False
            break
        elif exit == "Нет":
            break
        else:
            print("Введиет пожалуйста либо (Да) либо (Нет)!!!")
            continue