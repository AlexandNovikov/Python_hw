## Первый семинар
# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
    
#     *Пример:*
    
#     - 6 -> да
#     - 7 -> да
#     - 1 -> нет
# 2. Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# 3. Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт 
# номер четверти плоскости, в которой находится эта точка 
# (или на какой оси она находится).
    
#     *Пример:*
    
#     - x=34; y=-30 -> 4
#     - x=2; y=4-> 1
#     - x=-34; y=-30 -> 3
# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


# 5. Напишите программу, которая принимает на вход координаты двух 
# точек и находит расстояние между ними в 2D пространстве.
    
#     *Пример:* 
    
#     - A (3,6); B (2,1) -> 5,09
#     - A (7,-5); B (1,-1) -> 7,21

## второй семинар

1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

*Пример:*

- 6782 -> 23
- 0,56 -> 11
2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

*Пример:*

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

*Пример:*

- Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}
4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
не использовать random.randint и вообще библиотеку random
Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

ДЗ семинар 3

Домашнее задание оформляйте в виде возвращающих функций. Помните: то, что выдает ваша функция, может быть использовано в дальнейшем или выведено куда-то кроме консоли.

1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

*Пример:*

- [1.1, 1.2, 3.1, 5.567, 10.03] => 0.564 или 564
4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.

*Пример:*

- 45 -> 101101
- 3 -> 11
- 2 -> 10
5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

*Пример:*

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/sH87m)

#Домашняя работа 4
1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.

Пример:

- при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1
2- Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Посмотрели, что такое множество? Вот здесь его не используйте.

3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
Пример: при N = 12 -> [2, 3]

4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
В файле содержится, например:
Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
Это на случай возникновения непонятных символов в файле.

# домашняя работа 5
1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'абвгдейка - это передача' = >" - это передача"
2- Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
['python', 'c#']
[1,2]
Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
[(1,'PYTHON'), (2,'C#')]
Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
[сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
[(1,'PYTHON'), (102,'C#')]
Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах

#семинар 6
Формат: Объясняет преподаватель

Задача: предложить улучшения кода для уже решённых задач:

- С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce

1- Определить, присутствует ли в заданном списке строк, некоторое число
2- Найти сумму чисел списка стоящих на нечетной позиции
3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)
4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
Примеры
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1
5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
6-Сформировать список из  N членов последовательности.
Для N = 5: 1, -3, 9, -27, 81 и т.д.

Полезная информация
Допустим, у вас есть функция.
def is_int(input_number:str):
'''
Проверяет аргумент на принадлежность к int
params:input_number - введенное значение
return: int или False
'''
try:
input_number = int(input_number)
return input_number
except ValueError:
return False
Вы можете использовать эту функцию в лямбде. Делается это, примерно, вот так:
┌────────────────────────────┐
│lambda input_number: is_int(input_number) │
└────────────────────────────┘
или даже необязательно называть это input_number:
┌────────────────┐
│lambda char: is_int(char)│
└────────────────┘