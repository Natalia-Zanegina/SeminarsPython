from random import randint
import math
from tkinter import N
# Задача 1. Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

# print(math.pi)

# d = 0.001
# precision = len(str(d - int(d))) - 2
# result = (int(math.pi * (10 ** precision)))/10 ** precision
# print(result)


# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

# num = int(input('Введите натуральное число N: '))

# dividers = []
# for i in range(2, num + 1):
#     while num % i == 0:
#         num //= i
#         dividers.append(i)

# print(dividers)

# Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

# elements = []
# count = 9
# for i in range(count):
#     elements.append(randint(0,9))
# print(elements)   

# unique_and_first_occurence = []
# repeating_occurence = []
# for i in elements:
#     if i not in unique_and_first_occurence:
#         unique_and_first_occurence.append(i)
#     else:
#         repeating_occurence.append(i)

# result = []
# for i in elements:
#     if i not in repeating_occurence:
#         result.append(i)
# print(result)


# Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# num = int(input('Задайте натуральную степень k: '))

# coefficients = []
# for i in range(num + 1):
#     coefficients.append(randint(0,100)) 

# polynomial = str() 
# for i in range(num, -1, -1):
#     if i == 0:
#         polynomial += ('{}'.format(coefficients[i]))   
#     elif i == 1:
#         polynomial += ('{}x + ' .format(coefficients[i]))
#     else:
#         polynomial += ('{}x^{} + ' .format(coefficients[i], i))

# print(polynomial)

# data = open('task_4.txt', 'w')
# data.writelines(polynomial)
# data.close()

# Задача 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# dict = {}
# keys = dict.keys()

# def Degrees_and_Coefficients(polynomial, dictionary):
#     for i in range(1, len(polynomial)):
#         if polynomial[i] == '^':
#             if int(polynomial[i + 1]) not in keys:
#                 dictionary[int(polynomial[i+1])] = 0
#             digit = 1
#             j = i-2
#             while polynomial[j] != ' ' and j >= 0:
#                 dictionary[int(polynomial[i+1])] += (int(polynomial[j]) * digit)
#                 digit *= 10
#                 j = j-1
#         elif polynomial[i] == 'x' and (polynomial[i + 1] == ' ' or i == len(polynomial) - 1):
#             if 1 not in keys:
#                 dictionary[1] = 0
#             digit = 1
#             j = i-1
#             while polynomial[j] != ' ' and j >= 0:
#                 dictionary[1] += (int(polynomial[j]) * digit)
#                 digit *= 10
#                 j = j-1
#     k = len(polynomial)-1
#     digit = 1
#     while polynomial[k] != ' ':
#         if i != 'x':
#             if 0 not in keys:
#                 dictionary[0] = 0
#             j = k
#             if polynomial[j] == '^':
#                 dictionary[0] = 0
#                 break
#             dictionary[0] += (int(polynomial[j]) * digit)
#             digit *= 10
#             j = j-1
#             k -= 1
#     return dictionary

# path = 'task_5_1.txt'
# data = open(path,'r')
# for line in data:
#     dict = Degrees_and_Coefficients(line, dict)
# data.close()

# path = 'task_5_2.txt'
# data = open(path,'r')
# for line in data:
#     dict = Degrees_and_Coefficients(line, dict)
# data.close()

# polynomial = str() 
# for i in range(max(keys), min(keys), -1):
#     if i not in keys:
#         continue
#     polynomial += ('{}x^{} + ' .format(dict[i], i))
# polynomial += ('{}'.format(dict[min(keys)]))
# print(polynomial)

