#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#o 45 -> 101101
#o 3 -> 11
#o 2 -> 10


number = int(input('введите число: ')) 
x = ''
while number > 0:
    x = str(number % 2) + x
    number = number // 2
print(f'двоичное число  =  {x}')


