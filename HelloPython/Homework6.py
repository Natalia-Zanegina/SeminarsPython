from random import randint

# Семинар 2, задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def find_elements(x):
#     if x == 1:
#         return 1
#     else: return x * find_elements(x - 1)

# num = int(input('Введите число N: '))
# items = [find_elements(x) for x in range(1, num + 1)]
# print(items)

# Семинар 2, задача 3. Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

# num = int(input('Введите число k: '))
# elements = [(1 + 1/(x + 1)) ** (x + 1) for x in range(num)]
# print(elements)
# result = sum(elements)
# print(result)

# Семинар 3, задача 1. 
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

# items = [randint(0,9) for x in range(5)]
# print(items)
# elements_to_find = [items[x] for x in range(1, len(items), 2)]
# result = sum(elements_to_find)
# print(result)

# Другой (явно неоптимальный) способ (зато с использованием filter :) )
# items = [randint(0,9) for x in range(5)]
# print(items)
# def element_for_index(num):
#     global items
#     return items[num]
# elements_to_find = list(map(element_for_index, filter(lambda x: x%2, range(len(items)))))
# result = sum(elements_to_find)
# print(result)

# Семинар 3, задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# items = [2, 3, 4, 5, 6]
# result = [items[x] * items[-x-1] for x in range(int(len(items)/2)+1) if len(items)%2 or x != len(items)/2]
# print(result)

# Семинар 3, задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# def fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     elif n < 1:
#         return fibonacci(n + 2) - fibonacci(n + 1)
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# num = int(input('Введите число: '))
# items = [x for x in range(-num, num + 1)]
# result = list(map(fibonacci, items))
# print(result)
