'''
Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена, а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров.
Пример: 
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета. 
Output: Общая цена 9 рублей 60 копеек
'''

def total_sum(m, n, s):
	countRub = m * s
	countKop = n * s
	if countKop >= 100:
		countRub = countRub + (countKop // 100)
		countKop = countKop % 100
	return "Общая цена {} рублей {} копеек".format(countRub, countKop)  # write return value here

if __name__ == '__main__':
	m, n, s = int(input("Цена одной вещи\nрублей: ")), int(input("копеек: ")), int(input("количество: "))
	print(total_sum(m, n, s))
