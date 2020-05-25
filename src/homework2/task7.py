'''
Найти действительные корни уравнения AX^2+ Bx+C=0
'''
print("Введите a, b, c  для квадратного уравнения ax**2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = b ** 2 - 4 * a * c
print("Дискриминант:", discr)
if discr > 0:
  x1 = (-b + discr**0.5) / 2 * a
  x2 = (-b - discr**0.5) / 2 * a
  print("x1:", x1, "\nx2:", x2)
elif discr == 0:
  x = -b / (2 * a)
  print("x:", x)
else:
    print("В уравнении нет корней, т.к. дискриминант < 0")
	
'''
ввести список чисел, список произвольной длинны.
--Определить сколько чисел в списке четных , а сколько нечетных
-- Нужно проверить, все ли числа в последовательности уникальны.
Окончание ввода -0
'''


listA = list()
while True:
  a = input("Введите список чисел через пробел: ")
  if a == "0":
    break
  else:
    listA.append(a)
  print(listA)

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

listA = set(listA)
print("Уникальные числа последователбьности: ", listA)

'''
Заполнить квадратный двумерный массив. Размерность массива вводит с клавиатуры
'''

listA = list([])
a = int(input("Введите длинну массива: "))
b = int(input("Введите ширину массива: "))
for i in range(a):
  listA.append([1]*b)
for i in range(a):
  for j in range(b):
    if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
      listA[i][j] = 0
print(listA)



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
            n = ''
if n != "":
    cifri.append(n)
print(cifri)


'''
Написать функцию, которая для произвольной введенной строки (латинский алфавит) будет определять: 
	- количество гласных
	- количество согласных
	- количество пробелов
Возвращать полученные значения функция должна через return. Вывод значений на экран должен выполнятся в основной программе
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