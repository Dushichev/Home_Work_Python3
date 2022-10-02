#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#o [2, 3, 4, 5, 6] => [12, 15, 16];
#o [2, 3, 5, 6] => [12, 15]


spisok_one = [1,3,7,-1,4]
spisok_two = [2,5,3,-7,12]

def spisok_mult(spisok):
    new_lst = len(spisok)//2 + 1
    if len(spisok) %2 != 0: 
        len(spisok)//2
        new_lst = [spisok[i]*spisok[len(spisok)-i-1] for i in range(new_lst)]
    print(new_lst)

spisok_mult(spisok_one)
spisok_mult(spisok_two)