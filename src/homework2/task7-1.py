'''
Найти действительные корни уравнения AX^2+ Bx+C=0
'''
print("Введите a, b, c  для квадратного уравнения ax**2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
discr = b ** 2 - 4 * a * c
print("Дискриминант:", discr)
if discr > 0:
    x1 = (-b + discr**0.5) / 2 * a
    x2 = (-b - discr**0.5) / 2 * a
    print("x1:", x1, "\nx2:", x2)
elif discr == 0:
    x = -b / (2 * a)
    print("x:", x)
else:
    print("В уравнении нет корней, т.к. дискриминант < 0")