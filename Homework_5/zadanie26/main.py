#Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def triangle_number(n):
    if n == 0:
        return 0
    else:
        return n + triangle_number(n-1)

n = int(input("Введите число: "))
print(f"Факториал числа {n}: {factorial(n)}")
print(f"Треугольное число для {n}: {triangle_number(n)}")

