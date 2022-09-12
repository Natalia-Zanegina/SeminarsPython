# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Ответ записать в файл


num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

def find_div(n):
    dividers = []

    for i in range(2, n + 1):
        while n % i == 0:
            n //= i
            dividers.append(i)
    return dividers

print(find_div(num1))
print(find_div(num2))

