'''
Ввести список чисел, список произвольной длинны.
-- Определить сколько чисел в списке четных , а сколько нечетных
-- Нужно проверить, все ли числа в последовательности уникальны.
'''

inp = input("Введите числа: ")
listA = inp.split()
even = 0
odd = 0
for c in listA:
    c = int(c)
    if not c % 2:
        even += 1
    else:
        odd += 1
print("Четных чисел:", even)
print("Нечетных чисел:", odd)

listB = []
for el in listA:
    n = listA.count(el)
    if n >= 1:
        if (not el) in listB:
            listB.append(el)
print("Уникальные числа", listB)
