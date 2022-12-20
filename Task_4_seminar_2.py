# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] 
# - списко на основе n, а позиции элементов lst2=[3,1].

n = int(input("Input N: "))

list1 = []

import random                            # подключаем random с помощью инструкции

for i in range(n):
    c = random.randint((n*-1),n)         #указываем диапазон генерации случайных чисел: от -n до n
    list1.insert(i, c)
print(list1)

list2 = []
for j in range(2):
    x = random.randint(1, n-1)
    list2.insert(j,x)
print(list2)


composition = list1[list2[0]]*list1[list2[1]]
print(f'Сумма элементов, находящися под индексами {list2[0]} и {list2[1]} составляет {composition}')




        
        



