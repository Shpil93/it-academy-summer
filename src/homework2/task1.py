'''
Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена, а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров. 
Пример: 
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета. 
Output: Общая цена 9 рублей 60 копеек
'''

def total_sum(m, n, s):
  """Подсчет общей суммы покупок.

    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. формат:
        'x rubles y kopecks'
    """
    # write your code here
  
  countRub = m * s
  countKop = n * s
  if countKop >= 100:
    countRub = countRub + (countKop // 100)
    countKop = countKop % 100
  return "Общая цена {} рублей {} копеек".format(countRub, countKop)  # write return value here


if __name__ == '__main__':
  # здесь можно сделать ввод из консоли и проверить работу функции
  m, n, s = int(input("Цена одной вещи\nрублей: ")), int(input("копеек: ")), int(input("количество: "))
  print(total_sum(m, n, s))
