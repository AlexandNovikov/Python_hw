# 1- Вычислить число c заданной точностью d. Число Пи не просто 
# обрезать с math.pi, а вычислить, используя формулы: Нилаканта, 
# ряды Тейлора, серию Ньютона или серию Чудновских.

# Пример:

# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

# from math import *

# n = round(pi, 3)
# print('число Пи из функции Pi:', n)

# n = 100
# calc_pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) 
# for x in range(n))

# print('вычесленное число Пи:', round(calc_pi,3))



# 2- Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности. Посмотрели, что такое множество? Вот здесь его не используйте.
# from enum import unique
# from tokenize import Number
# Number=[1,5,5,5,6,6,7,7,8,9,10]
# unique_numbers = list(set(Number))
# print(unique_numbers, end = '')

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# subs = [1, 3, 5, 4, 9, 14, 5, 1]
# alone = []
# for i in range (0, len(subs)):
#     duplicate = 0
#     for j in range(0, len(subs)):
#         if i != j:
#             if subs[i] == subs[j]:
#                 duplicate = 1
#     if duplicate == 0:
#         alone.append(subs[i])
# print(alone)


# import os
# import random 
# os.system('cls')

# list = [random.randint (1, 100 ) for i in range (1, 30)]
# print('Исходная случайная последовательность: ')
# print(list)
# listing1 = []
# listing2 = []
# for i in list:
#     if list.count(i) == 1:
#         listing1.append(i)
#     else:
#         listing2.append(i)
# print('\nСписок неповторяющихся элементов: ')
# print(listing1)
# print('\nСписок повторяющихся элементов: ')
# print(listing2)


# 3- Задайте натуральное число N. Напишите программу, которая составит 
# список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

# mult = []
# num = int(input("Введите число N: "))
# for n in range(2, num):
#     if num % n == 0:
#         mult.append(n)

# print(mult)



# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

# https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
# Это на случай возникновения непонятных символов в файле.

# def check(f):
#     for i in f:
#         if i.isdigit():
#             return False
#     return True

# with open("file_HW_semi4.txt", "r") as file_HW_semi4:
#     a = file_HW_semi4.read().split()
# with open("file_HW_semi4.txt", "w") as file_HW_semi4:
#     for i in a:
#         if check(i):
#             file_HW_semi4.write(i+" ")