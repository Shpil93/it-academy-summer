'''
Ввести строку с клавиатуры. Выбрать из строки цифры
'''


a = input("Введите строку: ")
cifri = []
n = ""
for i in a:
    if "0" <= i <= "9":
        n = n + i
    else:
        if n != "":
            cifri.append(n)
            n = ""
if n != "":
    cifri.append(n)
print(cifri)
