'''
Написать функцию, которая для произвольной введенной строки (латинский алфавит) будет определять: 
	- количество гласных
	- количество согласных
	- количество пробелов
Возвращать полученные значения функция должна через return.
Вывод значений на экран должен выполнятся в основной программе.
'''


def vowel_count(str):
    countGl = 0
    countSogl = 0
    countPr = 0
    gl = set("aeiouAEIOU")
    sogl = set("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ")
    pr = set(" ")
    for alphabet in str:
        if alphabet in gl:
            countGl = countGl + 1
        elif alphabet in sogl:
            countSogl = countSogl + 1
        elif alphabet in pr:
            countPr = countPr + 1
    return countGl, countSogl, countPr

str = input("Введите строку: ")
a, b, c = vowel_count(str)
print("Гласные:", a, "\nСогласные:", b, "\nПробелы:", c)