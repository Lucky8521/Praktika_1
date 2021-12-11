el_C = 2
el_H = 6
el_O = 1
"""Функция spirt, нахождения максимального числа малекула спирта"""
def spirt():
    mas = dict()
    mas_1 = []
    element = 0
    l = 0
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            line = line.split(';')
            for i in line:
                spl_3 = i[2:]
                spl_4 = i[0:1]
                element += 1
                mas[element] = {"elem":spl_4,"kol":int(spl_3)}
        for q in mas:
            l = mas[q]["kol"]
            if mas[q]["elem"] == "C":              
                kol_vo = l // el_C
            if mas[q]["elem"] == "H":
                kol_vo = l // el_H
            if mas[q]["elem"] == "O":
                kol_vo = l // el_O
            mas_1.append(kol_vo)
        minimal = min(mas_1, key=lambda i: int(i))
        print(min(mas_1, key=lambda i: int(i)))
    output_file = open("Output.txt", "w")
    output_file.write(str(minimal) + "\n")
    output_file.close()
spirt()