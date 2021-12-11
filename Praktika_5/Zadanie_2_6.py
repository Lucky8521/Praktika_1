import re
import stdiomask
"""Функция passwd(), проверка пароля"""
def passwd(password):
        if len(password) < 6:
            print("Вы ввели пароль менее 6 символов! ")
            return False
        if password.isdecimal():
            print("Пароль не может состоять только из цифр")
            return False
        #Поиск если хотя бы 1 число в пароле.
        keks =  re.search('[0-9]', password)
        if not keks:
            print("Пароль должен содержать хотя бы одну цифру!")
            return False
        #Проверяет на ввод password.
        keks_2 =  re.search('[pP][aA][sS][sS][wW][oO][rR][dD]', password)
        if keks_2:
            print("Пароль не должен быть password: ")
            return False
        return True
while True:
        # a = getpass.getpass('Введите пароль: ')
        #Для отображения пароля *
        a = stdiomask.getpass('Введите пароль: ')
        if  passwd(a) == True:
            print("Вы успешно ввели пароль!")
            break
            

