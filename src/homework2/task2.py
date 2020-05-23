"""Найти самое длинное слово в введенном предложении. В случае если их
    несколько, самое левое в строке Учтите что в предложении есть знаки
    препинания.
"""


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """
    # write your code here
    znaki = '!?.,+=:;|/*<>[]{}@#$%^&()_'
    for i in str_:
        if i in znaki:
            str_ = str_.replace(znaki, "")
    listA = str_.split()

    idWord = 0
    for i in range(1, len(listA)):
        if len(listA[idWord]) < len(listA[i]):
            idWord = i


    return "Самое длинное слово в предложении", listA[idWord]


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = input("Введите строку через пробел: ")
    print(longest_word(str_))
