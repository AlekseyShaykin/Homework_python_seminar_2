# адайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = int(input("Input N: "))

list = []

for i in range(n):
    element = (1+1/n)**n
    list.insert(i, element)
print(list)


sum = 0
for j in range(len(list)):
    sum = sum+list[j]
sum2 = round(sum,2)

print(f'The sum = {sum2}')
