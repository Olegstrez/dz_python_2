
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import os
os.system('cls' if os.name == 'nt' else 'clear')
n = int(input("Введите N ="))
list_1 = [int (i) for i  in range(-n,n+1)]
print (list_1)
number = input("Введите умножаемые позиции через пробел ").split(" ")
new_number = list(map(int,number))
print (list(new_number))
result = list_1[new_number[0]]*list_1[new_number[1]]
print(result)
