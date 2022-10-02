#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#Пример:
#o для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#[Негафибоначчи]


number = int(input("введите число \n")) 
number_1 = 0
number_2 = 1
list_fibonachi =[0,1]
list_fibonachi_minus = []
for i in range(1, number):
        number_1, number_2 = number_2, number_1 + number_2
        list_fibonachi.append(number_2)
        list_fibonachi_minus.append(-number_2)
list_fibonachi_minus.reverse()
summa_list = list_fibonachi_minus + list_fibonachi
print(summa_list)    
