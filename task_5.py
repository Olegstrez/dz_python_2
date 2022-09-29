# Реализуйте алгоритм перемешивания списка.
import random
import os
os.system('cls' if os.name == 'nt' else 'clear')
lst = [random.randint(0,10) for i in range(random.randint(5,20))]
print(f"исходный список:\n {lst}")
random.shuffle(lst)
print(f"после список:\n {lst}")