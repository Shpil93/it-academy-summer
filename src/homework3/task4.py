'''
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами. 
Выходные данные - количество пар. 
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
'''


str = "1 2 3 4 5 6 7 1 2 3 4 5 8 9 1"
lst = str.split()
print(lst)
new_lst = []
for i in lst:
    cnt = lst.count(i)
    if cnt == 1:
        new_lst.append(i)
print(new_lst)
