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