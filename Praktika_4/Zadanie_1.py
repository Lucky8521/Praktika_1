from random import randint
a = 5 
b = []
"""Заполнение рандомно числе в список"""
for i in range(a):
   b.append(randint(1, 20))
print(b)
"""Раставление списка в порядке возрастания. Метод пузырька"""
for i in range(a-1):
    for j in range(a-i-1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
print(b)

