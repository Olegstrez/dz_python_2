# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:

# - 0,56 -> 11
import os
os.system('cls' if os.name == 'nt' else 'clear')
num = (input("Введите число "))
list1 = [int(a) for a in str(num)]
print(sum(list1))

