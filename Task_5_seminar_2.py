# Реализуйте алгоритм перемешивания списка. 
# (рандомно поменять местами элементы списка между собой)

n = int(input("Input quantitiy of elements: "))
list1 = []

import random

for i in range(n):
    list1.insert(i, random.randint(0,20))
print(f'Исходный список: {list1}')


random.shuffle(list1)                      # перемешиваем список list1
print(f'Перемешали: {list1}')

