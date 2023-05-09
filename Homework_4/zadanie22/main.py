# Задача 22: Даны два неупорядоченных набора целых чисел
# (может быть, с повторениями). Выдать без повторений в
# порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого
# множества. m — кол-во элементов второго множества.

import random
n = int(input("Введите число n - кол-во элементов первого множества: "))
m = int(input("Введите число m -  кол-во элементов второго множества: "))
print()

firstList = []
secondList = []
resultList = []

i = 0
while i < n:
    firstList.append(random.randint(1, 21))
    i += 1
print(f"Первый набор чисел: {firstList}")

i = 0
while i < m:
    secondList.append(random.randint(1, 21))
    i += 1
print(f"Второй набор чисел: {secondList}")
print()

gluedltList = firstList + secondList

for j in range(len(gluedltList)):
    for k in range(len(gluedltList) - 1):
        if gluedltList[k] > gluedltList[k + 1]:
            gluedltList[k], gluedltList[k + 1] = gluedltList[k + 1], gluedltList[k]

resultList.append(gluedltList[0])
i = 1
while i < n + m:
    if gluedltList[i] != gluedltList[i - 1]:
        resultList.append(gluedltList[i])
    i += 1
print(f"Итоговый набор чисел без повторений: {resultList}")