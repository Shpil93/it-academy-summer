'''
Ввести строку с клавиатуры. Выбрать из строки цифры
'''

a = input("Введите строку: ")
cifri = []
n = ""
for i in a: #проходим циклом по строке
    if "0" <= i <= "9": #выбираем числа
        n = n + i
    else:
        if n != "":
            cifri.append(n)
            n = ""
if n != "":
    cifri.append(n)
print(cifri)