from random import randint
import math 
# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

# str_num = input('Введите вещественное число: ')
# num = float(str_num)
# int_digits = str(int(num))

# digits_after_comma = len(str_num) - len(int_digits) - 1
# new_num = int(round(num, digits_after_comma) * 10 ** digits_after_comma)

# sum = 0
# while new_num > 0:
#     sum += new_num % 10
#     new_num //= 10

# print(sum)



# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input('Введите число N: '))
# result = []
# mult = 1
# for i in range(num):
#     result.append(mult * (i + 1))
#     mult *= (i + 1)

# print(result)



# Задача 3. Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

# num = int(input('Введите число k: '))
# elements = []
# for i in range(num):
#     elements.append((1 + 1/(i + 1)) ** (i + 1))

# print(elements)
# sum = 0
# for i in range(num):
#     sum += elements[i]

# print(sum)



# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# num = int(input('Введите число N: '))
# elements = []

# for i in range(num):
#     elements.append(randint(-num, num))

# print(elements)

# str_positions = input('Введите через пробел позицию первого элемента, второго элемента: ')
# parsed_positions = str_positions.split()
# print('Произведение элементов на указанных позициях равно {}'.format(elements[int(parsed_positions[0])] * elements[int(parsed_positions[1])]))

# Задача 5. Реализуйте алгоритм перемешивания списка.

# nums = [1111, 23, 348889, 4, 55, 67777777, 0.8, -0.8]
# print(nums)

# for i in range(len(nums)):
#     temp = nums[i]
#     new_index = randint(0, len(nums)-1)
#     nums[i] = nums[new_index]
#     nums[new_index] = temp

# print(nums)