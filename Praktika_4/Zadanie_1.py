from random import randint
a = 5 
b = [9, 8, 7 , 6 , 5]
for i in range(a):
   b.append(randint(1, 20))
print(b)

for i in range(a - 1):
    #print (i)
    for j in range(a-i -1):
        if b[j] > b[j+1]:
            b[j], b[j+1] = b[j+1], b[j]
    print(b)
print(b)

