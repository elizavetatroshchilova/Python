# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

totalCranes = int(input("Введите чётное количество сделанных журавликов: ")) 
resultPete = 0
resultKate = 0
resultSerj = 0
print()

if totalCranes % 2 != 0:
    print()
    print("Введённое количетсво журавликов нечётное!")
else:
    resultPete = totalCranes / 6
    resultSerj = resultPete
    resultKate = (resultPete + resultSerj) * 2
    print(f"Петя сделал журавликов: {int(resultPete)}")
    print(f"Катя сделала журавликов: {int(resultKate)}")
    print(f"Серёжа сделал журавликов: {int(resultSerj)}")