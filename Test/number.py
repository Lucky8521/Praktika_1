def funk_add(a, b):
        # a = float(input('Введите число а: '))
        # b = float(input('Введите число b: '))
        """Возращает первое истиное значение!"""
        if (a == float or b == float):
            raise  Exception
        return a+b

def funk_sub(a, b):
    return a - b
def funk_mul(a, b):
    return a * b
def funk_div(a, b):
    if b == 0:
        print("Делить на ноль не льзя!!")
    else:
        return a / b
def funk_Rem(a, b):
    return a % b 
def funk_Parts(a, b):
    return a//b