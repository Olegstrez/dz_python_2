# Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

import math
import os
os.system('cls' if os.name == 'nt' else 'clear')
k = int(input("Введите число "))
list1 = []
for i in range(1,k+1):
    x = math.pow((1+1/i),i)
    list1.append(x)
print (list1)
print (sum(list1))