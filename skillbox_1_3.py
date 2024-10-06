# Задача 1. Квадраты превратились в кубы
# Напишите программу, которая выводит кубы чисел (число в третьей степени), лежащих в диапазоне от 1 до 10.
#
# Результат:
#
# 1
# 8
# 27
# 64
# 125
# 216
# 343
# 512
# 729
# 1000
for i in range(1, 11):
    print(i**3)

print()
#
#
# Задача 2. Сумма чисел
# Напишите программу, где пользователь вводит любые два целых положительных числа.
# А программа суммирует все числа в диапазоне от первого до второго.
# Гарантируется, что первое введённое число всегда меньше второго.
#
# Пример:
#
# Введите первое число: 5
# Введите второе число: 10
# Сумма чисел от 5 до 10 равна 45

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
summ = 0
for i in range(a, b + 1):
    summ += i
print(summ)

print()
#
#
# Задача 3. Поел — можно и поспать, поспал — можно и поесть
# Напишите программу, разобранную в уроке.
#
# У Саши интересный режим сна: он может проснуться когда угодно, хоть ночью,
# но засыпает всегда до того, как наступит полночь, обычно в 23 часа.
# А ещё он очень любит поесть. Он ест каждый час и если съедает больше 2000 калорий,
# то он просто падает спать. Напишите программу, которая поможет Саше понять, всё ли с ним хорошо.
# Для этого нужно посчитать, сколько он всего съест калорий и сколько часов будет бодрым.

wake_up = int(input("Во сколько проснулся? "))
awake_hours = 0
calories_sum = 0
for hour in range(wake_up, 23):
    print("Сейчас", hour, "часов")
    calories = int(input("Сколько съел за час? "))
    calories_sum += calories
    if calories_sum > 2000:
        print("Хорошо поел, можно и поспать")
        break
    awake_hours += 1

print("Съедено калорий за день: ", calories_sum)
print("Часов не спал: ", awake_hours)
