# # Реализуйте алгоритм задания случайных чисел
# # без использования встроенного генератора псевдослучайных чисел.


# # from datetime import datetime as dt

# # def my_random(min, max):
# #     rnd = dt.now().microsecond
# #     scale = max - min
# #     return int(rnd/1000000 * scale + min)

# # print(my_random(10, 50))


# # ----------------
# # from datetime import datetime

# # print(datetime.now().microsecond % 10)

# # ---------------------------------------------------------------------
# # Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# # my_list = ["123", "234", '123', "567", '5', '8']

# # f=int(input("число: "))

# # def check_num(number,lists):
# #     return str(number) in lists or number in lists


# # print(check_num(f,my_list))

# # Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.


# list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"] # "qwe" 3
# list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"] # "йцу" 5
# list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"] # "йцу" -1
# list4 = ["123", "234", 123, "567"] # 123 -1
# list5 = [] # -1




# def find_second(str, lst):
#     if lst.count(str) > 1:
#         return lst.index(str, lst.index(str) + 1)
#     return "-1"

# print(find_second("qwe", list1))


#Для натур число n создать множество: от 0 до n
# -3 ==> [1, -3, 9, -27, 81]


# def give_me_mnojestvo(N):
#     return [(-3) ** i for i in range(N)]

# print(give_me_mnojestvo(5))

# n = int(input('Введите число: '))
# print([((-3)**i) for i in range(n)])

# Сформировать сисок из N членов последовательности. 
# Список записать в файл "number_list.txt" (в одну строку - одно число).

from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE


def give_me_mnojestvo(N):
    return [(-3) ** i for i in range(N)]

file_name = "numbers_list.txt"
lst = give_me_mnojestvo(5)
with open(file_name, 'w') as file:
    for item in lst:
        file.write(f'{item}\n')

a=[]

print(dir(a))