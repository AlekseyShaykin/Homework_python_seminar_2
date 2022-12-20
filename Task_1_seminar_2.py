# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

x = float(input('Input number: '))
text = str(x)

sum = 0
for char in text:
    if char.isdigit():
        sum += int(char)
        
print(f'Sum = {sum}')


