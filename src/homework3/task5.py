'''
Дан список. Выведите те его элементы,
которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке,
в котором они встречаются в списке.
'''


lst = [1, 2, 3, 4, 5, 1, 5]
new_lst = []
for i in lst:
    cnt = lst.count(i)
    if cnt == 1:
        new_lst.append(i)
print(new_lst)
