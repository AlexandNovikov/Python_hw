# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

# text = 'абвгдейка - это передача'


# def del_words(text):
#     text = list(filter(lambda x: 'абв' not in x, text.split()))
#     return " ".join(text)


# text = del_words(text)
# print(text, '\n')

# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.

# import random

# playerOne = input('Введите имя первого игрока ')
# playerTwo = input('Введите имя второго игрока ')

# firstunnumber = random.randint(1, 100)
# secturnnumber = random.randint(1, 100)

# if( firstunnumber > secturnnumber): print(f'{playerOne} ходит первый')
# else: print(f'{playerTwo} ходит первый')

# num2 = 2021
# n = 0
# while num2 > 0:
#     num1 = int(input('Введите число до 28: '))
#     if num1 > 28: print('неверно, число должно быть меньше 28!')
#     else: 
#         num2 -= num1
#         print(f'Осталось {num2} конфет')
#         n = n+1
# if(n%2==0): print(f'Выиграл {playerTwo}')
# else: print(f'Выиграл {playerOne}')

# a) Добавьте игру против бота

# import random

# num2 = 40
# while num2 > 0:
#     num1 = int(input('Введите число до 28: '))
#     if num1 > 28: print('неверно, число должно быть меньше 28!')
#     else: 
#         num2 -= num1
#         if num2 <= 0: print('Вы выиграли!')
#         else: 
#             comp = random.randint(1, 28)
#             print(f'Компьютер выбрал {comp}')
#             num2 -= comp
#             if num2 <= 0: print('Выиграл бот')
#             print(f'Осталось {num2} конфет')

# b) Подумайте как наделить бота ""интеллектом""




# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

# from functools import reduce

# def create_num_name_cort(name, num):
#     result = list(zip(num, [i.upper() for i in name]))
#     return result

# def filter_points_name_cort(name, num):
#     result = [reduce(lambda x, y: x + ord(y), i, 0) for i in name]  
#     print(f'Список очков: {result}')    
#     result = [(result[i], name[i]) for i in range(len(num)) if result[i] % num[i] == 0] 
#     return result

# name_lang = ['C Sharp', 'Delphi', 'C', 'Go', 'Kotlin', 'Java']
# serial_num = [i + 1 for i in range(0, len(name_lang))]

# print(f'Исходный список: {create_num_name_cort(name_lang, serial_num)}')
# print(f'Cписок, отвечающий условию : {filter_points_name_cort(name_lang, serial_num)}')

# 4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах


def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string


with open('file_start.txt', 'r') as file:
    decoded_string = file.read()

with open('file_finish.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Входные данные: \t' + decoded_string)
print('Кодирование: \t' + rle_encode(decoded_string))
print(f'Мощность кодирования: \t{round(len(decoded_string) / len(encoded_string), 1)}')