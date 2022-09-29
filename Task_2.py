# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import os
os.system('cls' if os.name == 'nt' else 'clear')
n = int(input("Введите число "))
x = 1
list = []
for i in range(1,n+1):
    x *=i
    list.append(x)
print (list)
