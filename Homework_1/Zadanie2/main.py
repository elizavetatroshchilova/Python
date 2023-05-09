# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трёхзначное число: "))
result = 0
c = 0
b = 0
a = 0

if number < 100 or number > 999:
    print("Введённое число не является трёхзначным")
else:
    c = number % 10
    b = number // 10 % 10
    a = number // 100 % 10
    result = a + b + c

print()
print(f"сумма трёх чисел: {result}")