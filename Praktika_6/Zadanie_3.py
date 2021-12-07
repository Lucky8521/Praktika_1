import base64
# XOR для шифрования/расшифровки
def xor_cipher( str, key ):
    encript_str = ""
    a_list = [chr(ord(a) ^ ord(b)) for a,b in zip(str, key)]
    return a_list
chikal = True   
while chikal: 
    with open('input_2.txt', 'r', encoding='utf-8') as input_file: 
        for line in input_file:
            strg = line
            keyy = (input("Введите Ключ шифрования: "))
            print( "Оригинал:\t\t\t", strg )
            encr_strg = xor_cipher( strg, keyy ) 
            print( "Зашифровонное сообщение:\t", "".join(encr_strg) )
            output_file = open("Output_2.txt", "w", encoding='utf-8')
            output_file.write(str(encr_strg) + "\n")
            print( "Расшифрованное сообщение:\t", "".join(xor_cipher( encr_strg, keyy )))
    while True:
        clode = input("Хотите ли вы выйти? (Да/Нет)")
        if clode == "Да":
            chikal = False
        elif clode == "Нет": 
            break
        elif clode != "Да" or clode != "Нет":
                print("Введите либо да либо нет!!")


