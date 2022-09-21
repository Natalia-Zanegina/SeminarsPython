from random import randint
# Задача 2. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход 
# определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются 
# сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Игра против бота с интеллектом:

# def Users_steps():
#     global count
#     step = int(input('Сколько конфет Вы забираете? '))
#     count -= step
#     if count <= 0:
#         print("Вы выиграли!")
#     else:
#         print('Осталось {} конфет'.format(count))
        

# def Bots_steps():
#     global count, max_step
#     if count % (max_step + 1) !=0:
#         step = count % (max_step + 1)
#     else:
#         step = randint(1, 28)
#     print('Бот забрал {} конфет'.format(step))
#     count -= step
#     if count <= 0:
#         print('Вы проиграли!')
#     else:
#         print('Осталось {} конфет'.format(count))

# count = 2021
# max_step = 28

# input('Чтобы бросить жребий, нажмите Enter: ')
# lot = randint(0,1)

# if lot:
#     print('Первым ходите Вы.')
# else:
#     print('Первым ходит бот.')

# while count > 0:
#     if lot:
#         Users_steps()
#         if count > 0:
#             Bots_steps()
#     else:
#         Bots_steps()
#         if count > 0:
#             Users_steps()

# Игра человек против человека

# def Users_steps(user):
#     global count
#     print('Ходит {}: '.format(user))
#     step = int(input('Сколько конфет Вы забираете? '))
#     count -= step
#     if count <= 0:
#         print("Выиграл {}!".format(user))
#     else:
#         print('Осталось {} конфет'.format(count))

# count = 100
# max_step = 28
# user1 = 'первый игрок'
# user2 = 'второй игрок'

# while count > 0:
#     Users_steps(user1)
#     if count > 0:
#         Users_steps(user2)


# Задача 3. Создайте программу для игры в ""Крестики-нолики"".

# def Show_Matrix(m):
#     print()
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             print(m[i][j], end=' ')
#         print()
#     print()

# def Steps(sign, player):
#     global matrix
#     print('Ход игрока за {}.'.format(sign))
#     step_row = int(input('Введите номер строки: '))
#     step_column = int(input('Введите номер столбца: '))
#     while matrix[step_row][step_column] != '*':
#         print('Ошибка! Эта позиция уже занята.')
#         step_row = int(input('Введите номер строки: '))
#         step_column = int(input('Введите номер столбца: '))
        
#     matrix[step_row][step_column] = sign

#     if step_row == 0:
#         player.add(str(step_column))
#     elif step_row == 1:
#         player.add(str(step_column + len(matrix)))
#     else:
#         player.add(str(step_column + 2*len(matrix)))
    
#     Show_Matrix(matrix)

# def Checking(player):
#     global winning_combinations
#     for i in winning_combinations:
#         if i.issubset(player):
#             return True
#     return False

# matrix = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
# Show_Matrix(matrix)

# winning_combinations = [{'0', '1', '2'}, {'3', '4', '5'}, {'6', '7', '8'}, {'0', '3', '6'}, {'1', '4', '7'}, {'2', '5', '8'}, {'0', '4', '8'}, {'2', '4', '6'}]

# sign_x = 'X'
# sign_0 = '0'
# player_X = set()
# player_0 = set()

# for i in range(5):
#     Steps(sign_x, player_X)
#     if Checking(player_X):
#         print('Победили крестики!')
#         break
#     else:
#         if i != 4:
#             Steps(sign_0, player_0)
#             if Checking(player_0):
#                 print('Победили нолики!')
#                 break
#         else:
#             print('Ничья!')
    


# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные
# хранятся в отдельных текстовых файлах.

# Модуль сжатия
# task = str()

# path = 'data_task4.txt'
# data = open(path, 'r')
# for line in data:
#     task = line
# data.close()


# result = str()
# count = 1

# if len(task) == 1:
#     result += task[0] + str(len(task))
# elif len(task) != 0:
#     temp = task[0]
#     for i in range(1, len(task)):
#         if task[i] == temp:
#             count +=1
#         else:
#             result += task[i-1] + str(count)
#             temp = task[i]
#             count = 1
#     result += task[i] + str(count)

# with open('result_task4.txt', 'w') as data:
#     data.write(result)

# Модуль восстановления
# task = str()

# path = 'result_task4.txt'
# data = open(path, 'r')
# for line in data:
#     task = line
# data.close()

# task += ' '
# item = str()
# num = str()
# result = str()

# for i in task:
#     if not i.isdigit():
#         if len(num) != 0 or i == ' ':
#             result += int(num) * item
#             item = i
#             num = str()
#         else: item = i
#     else:
#         num += i

# with open('recovery_task4.txt', 'w') as data:
#     data.write(result)

