'''
Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz,
вместо чисел кратный 5 пишет Buzz,
а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
'''


for c in range(1, 101):
    if (c % 3 == 0) and (c % 5 == 0):
        print("FizzBuzz")
    elif (c % 5 == 0):
        print("Buzz")
    elif (c % 3 == 0):
        print("Fizz")
    else:
        print(c)
