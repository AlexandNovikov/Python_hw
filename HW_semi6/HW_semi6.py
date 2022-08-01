# Подсчитать сумму цифр в вещественном числе

# n = input('Введите вещественное число: ')
# sum = sum(map(int, n.replace('.', '')))
# print (sum)

#1- Определить, присутствует ли в заданном списке строк, некоторое число

# lst = ['съешь', 'ещё', 'этих', 'мягких', 'французских', 'булок,', 'да', 'выпей', 'чаю', '123', '456', '7890']
# num = input('что хотим найти? ')

# def num_in_lst(lst, number):
#     return list(filter(lambda elem: str(number) in elem, lst))

# print(num_in_lst(lst, num))

# 2. Найти сумму чисел списка стоящих на нечетной позиции

# n = int(input('n = '))
# print(sum(list(filter(lambda x: x%2, [x for x in range(1, n + 1)]))))

#3 Найти расстояние между двумя точками пространства(числа вводятся через пробел)
# from functools import reduce
# dot_1 = list(map(int, input('Введите две координаты первой точки: ').split()))
# dot_2 = list(map(int, input('Введите две координаты второй точки: ').split()))
# def dot_range(dot_1, dot_2):
#     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
#     return round(rng, 2)
# print(dot_range(dot_1, dot_2))

# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# desired = 'qwe'

# def second_in(lst, desired):
#     count = 0
#     for i, elem in enumerate(lst):
#         if elem == desired:
#             count += 1
#             if count == 2:
#                 break
#     if count > 0:
#         return i
#     else:
#         return -1

# print(second_in(lst, desired))

# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# lst = [2, 3, 4, 2, 5]

# def multy_bi(lst):
#     return [lst[i] * lst[len(lst)-1 -i] for i in range(len(lst)//2 + len(lst)%2)]

# print(multy_bi(lst))

#6 Сформировать список из  N членов последовательности
# c помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# N = int(input('Введите количество членов последовательности: '))

# list = [3**i if i % 2 == 0 else -3**i for i in range (N)]
# print(list)