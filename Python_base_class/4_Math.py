import math

x1 = 0
x2 = 0


def calculate(a, b, c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    return x1, x2

x1,x2 = calculate(-1, -2,3)

print(x1, x2)