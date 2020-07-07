'''
1 Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
2 Используйте на предыдущий список slice чтобы получить следующий:
['ab', 'ad', 'bc'].
3 Используйте генератор списков чтобы получить следующий:
['1a', '2a', '3a', '4a'].
4 Одной строкой удалите элемент '2a' из прошлого списка и напечатайте его.
5 Скопируйте список и добавьте в него элемент '2a' так,
чтобы в исходном списке этого элемента не было.
'''


sp1 = [c + d for c in ['a', 'b'] for d in ['b', 'c', 'd']]
print(sp1)

sp2 = sp1[::2]
print(sp2)

sp3 = [c + d for c in ['1', '2', '3', '4'] for d in ['a']]
print(sp3)

print(sp3.pop(1))

sp4 = sp1[:]
sp4.insert(0, '2a')
print(sp4, sp1)
