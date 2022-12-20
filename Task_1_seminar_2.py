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


# def Method(a):
#     x = int(a*10)
#     sum =0
#     if (a*10)-x == 0:
#            while a>0:
#             sum = sum + a%10
#             a = a//10
#     else:
#         while :
            
#             sum = sum+int(a)
#             a = 


#     return sum
   


# res = int(Method(x))
# print(f'{x} -> {res}')
