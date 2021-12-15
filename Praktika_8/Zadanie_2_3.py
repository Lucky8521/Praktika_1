"""Класс люди(человек)"""
class human():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.geder = gender
"""Класс student, Родитель human"""
class student(human):
    def __init__(self, name, age, gender, kol_pass_dz):
        super().__init__(name, age, gender)
        self.kol_pass_dz = kol_pass_dz
    
    '''равенство, проверка на равенство'''
    def __eq__(self, y):
        return self.kol_pass_dz.__eq__(y.kol_pass_dz)
    
    '''Проверка меньше ли первое второго'''
    def __lt__(self, y):
        return self.kol_pass_dz.__lt__(y.kol_pass_dz)
    
    '''Проверка больши первое, второго'''
    def __gt__(self, y):
        return self.kol_pass_dz.__gt__(y.kol_pass_dz)

stud = student("Виктор", 22, "М", 1)
stud_1 = student("Сергей", 23, 'М', 2)
if stud.__eq__(stud_1):
    print("cтудент " +str(stud.name)+ " cдал cтолько же работ сколько и cтудент " + str(stud_1.name))
elif stud.__gt__(stud_1):
    print("cтудент " +str(stud.name)+ " сдал больше заданий чем студент " + str(stud_1.name))
elif stud.__lt__(stud_1):
    print("cтудент " +str(stud.name)+ " сдал меньше заданий чем студент " + str(stud_1.name))