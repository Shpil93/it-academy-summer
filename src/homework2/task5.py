"""Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.
"""


def fibonacci(n):
    """Поиск числа фибоначчи.

    :param n: Номер числа Фибоначчи.
    :return: Число. n-ое число Фибоначчи
    """

    # write your code here
    """
    a0 = a1 = 1
    for i in range(n-2):
        a0, a1 = a1, a0 + a1
    return "N-ое число Фибоначчи: {}".format(a1)  # write return value here
    """

    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n+1)

if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = 0
    n = int(input("Введите n-ое число Фибоначчи: "))
    print(fibonacci(n))
