# 1- Вычислить число c заданной точностью d. Число Пи не просто 
# обрезать с math.pi, а вычислить, используя формулы: Нилаканта, 
# ряды Тейлора, серию Ньютона или серию Чудновских.

# Пример:

# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

from math import *

n = round(pi, 3)
print('число Пи из функции Pi:', n)

n = 100
calc_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) 
for x in range(n))

print('вычесленное число Пи:', round(calc_pi,3))



# 2- Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Посмотрели, что такое множество? Вот здесь его не используйте.


# 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]


# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

# https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
# Это на случай возникновения непонятных символов в файле.