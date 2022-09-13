from random import randint
# Задача 1. 
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

# items = []
# count = 5
# for i in range(count):
#     items.append(randint(0,9))
# print(items)

# sum = 0
# for i in range(count):
#     if i % 2 != 0:
#         sum += items[i]

# print(sum)



# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# elements = [9, 3, 2, -8, 6]
# result = []

# for i in range(len(elements) // 2):
#     result.append(elements[i] * elements[len(elements) - i - 1])

# if len(elements) % 2 != 0:
#     result.append(elements[len(elements) // 2] ** 2)

# print(result)


# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

# elements = [1.1, 1.2, 3.1, 10.01]

# fractional_part = []
# for i in range(len(elements)):
#     fractional_part.append(elements[i] - int(elements[i]))

# min_el = min(fractional_part)
# max_el = max(fractional_part)

# result = round(max_el - min_el, 2)
# print(result)


# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# num = int(input('Введите число: '))
# result = str()
# while num != 0:
#     result = str(num % 2) + result
#     num //= 2
# print(result)


# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
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
# result = []
# for i in range(-num, num + 1):
#     result.append(fibonacci(i))
# print(result)
