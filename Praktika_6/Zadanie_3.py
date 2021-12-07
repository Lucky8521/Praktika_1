import base64
# XOR для шифрования/расшифровки
def xor_cipher( str, key ):
    encript_str = ""
    for letter in str:
        encript_str += chr( ord(letter) ^ key )
    return  encript_str
chikal = True   
while chikal: 
    with open('input_2.txt', 'r', encoding='utf-8') as input_file: 
        for line in input_file:
            strg = line
    try:
            keyy = int(input("Введите Ключ шифрования: "))
            if keyy < 0:
                print("Число не должно быть отрицательным!!!")
                continue
            print( "Оригинал:\t\t\t", strg )
            encr_strg = xor_cipher( strg, keyy ) 
            print( "Зашифровонное сообщение:\t", encr_strg )
            output_file = open("Output_2.txt", "w", encoding='utf-8')
            output_file.write(str(encr_strg) + "\n")
            print( "Расшифрованное сообщение:\t", xor_cipher( encr_strg, keyy ) )
    except ValueError:
        print("Введите число!!!")
    while True:
        clode = input("Хотите ли вы выйти? (Да/Нет)")
        if clode == "Да":
            chikal = False
            break
        elif clode == "Нет": 
            break
        elif clode != "Да" or clode != "Нет":
                print("Введите либо да либо нет!!")


