'''
Дан список целых чисел.
Требуется переместить все ненулевые элементы в левую часть списка,
не меняя их порядок, а все нули - в правую часть.
Порядок ненулевых элементов изменять нельзя,
дополнительный список использовать нельзя,
задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
'''


lst = [9, 8, 7, 0, 5, 6, 0, 3, 2, 0, 1, 0]
for i in lst:
    if i == 0:
        lst.append(i)
        lst.remove(i)
print(lst)
