# Задача 1
# day = int(input('Введите номер дня недели: '))
# if (day == 6) or (day == 7):
#     print('Да')
# else:
#     print('Нет')

# Задача 2
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if (not(x or y or z)) != (not x and not y and not z):
#                 print(False)
#                 break
# print(True)

# Задача 3
# x = int(input('Введите координату x: '))
# y = int(input('Введите координату y: '))
# if (x > 0 and y > 0):
#     print('1')
# if (x < 0 and y > 0):
#     print('2')
# if (x < 0 and y < 0):
#     print('3')
# if (x > 0 and y < 0):
#     print('4')

# Задача 4
# quadrant = int(input('Введите номер четверти: '))
# if quadrant == 1:
#     print('x ∈ (0; +∞), y ∈ (0; +∞)')
# if quadrant == 2:
#     print('x ∈ (-∞; 0), y ∈ (0, +∞)')
# if quadrant == 3:
#     print('x ∈ (-∞; 0), y ∈ (-∞; 0)')
# if quadrant == 4:
#     print('x ∈ (0, +∞), y ∈ (-∞; 0)')

# Задача 5
# from math import sqrt
# x_a = int(input('Введите координату x точки A: '))
# y_a = int(input('Введите координату y точки A: '))
# x_b = int(input('Введите координату x точки B: '))
# y_b = int(input('Введите координату y точки B: '))
#
# dist = sqrt((x_b - x_a)**2 + (y_b - y_a)**2)
#
# print(dist)