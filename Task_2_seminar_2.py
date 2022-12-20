
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Input number: '))
print(f'{N}  factorial --> ')

# задали range  размером N+1 с шагом 1 причем ran имеет класс range
ran = range(1, (N+1), 1)

# этим действием мы приводим класс range переменной ran к классу list
list1 = list(ran)


per = 1
numbers = []
for i in list1:
    per = per*list1[i-1]
    numbers.insert(i, per)
print(numbers)
