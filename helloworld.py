# # # # # # # from re import A


# # # # # # # print('hello world')
# # # # # # # 997
# # # # # # # value = 123
# # # # # # # string = 'hi'
# # # # # # # print('Print a = ')
# # # # # # # a=int(input())

# # # # # # # print('Print b = ')
# # # # # # # b=int(input())
# # # # # # # # c=(a/b)
# # # # # # # # print('{}/{}={}'.format(a,b,c))
# # # # # # # line = ""
# # # # # # # for i in range(6):
# # # # # # #  line = ""
# # # # # # #  for j in range(20):
# # # # # # #     line += "+"
# # # # # # # #  print(line)
# # # # # # # text = 'съешь ещё этих мягких французских булок'
# # # # # # # print(len(text)) # 39
# # # # # # # print('ещё' in text) # True
# # # # # # # print(text.isdigit()) # False
# # # # # # # print(text.islower()) # True
# # # # # # # print(text.replace('ещё','ЕЩЁ')) #
# # # # # # # for c in text:
# # # # # # #  print(c)
# # # # # # text = 'съешь ещё этих мягких французских булок'
# # # # # # print(text[0]) # c
# # # # # # print(text[1]) # ъ
# # # # # # print(text[len(text)-1]) # к
# # # # # # print(text[-5]) # б
# # # # # # print(text[:]) # print(text)
# # # # # # print(text[:2]) # съ
# # # # # # print(text[len(text)-2:]) # ок
# # # # # # print(text[2:9]) # ешь ещё
# # # # # # print(text[6:-18]) # ещё этих мягких
# # # # # # print(text[0:len(text):6]) # сеикакл
# # # # # # print(text[::6]) # сеикакл
# # # # # # text = text[2:9] + text[-5] + text[:2] # ...

# # # # # # 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# # # # #     *Примеры:*

# # # # #     - 5, 25 -> да
# # # # #     - 4, 16 -> да
# # # # #     - 25, 5 -> да
# # # # #     - 8,9 -> нет
# # # # # """

# # # # # a=int(input("введите число:" ))
# # # # # b=int(input("введите число:" ))
# # # # # if a*a==b or b*b==a:
# # # # #     print("yes")
# # # # # else:
# # # # #     print("no")

# # # # # *****************************************************************************************************
# # # # # 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# # # # #     Примеры:

# # # # #     - 1, 4, 8, 7, 5 -> 8
# # # # #     - 78, 55, 36, 90, 2 -> 90

# # # # from random import Random


# # # # v={1,5,25,3,9}
# # # # f=0
# # # # for i in v:
# # # #     i>f
# # # #     f=i
# # # # print(f)


# # # # int[]z={1,2,3,4,}
# # # # -********************************************************************************************************************
# # # # """
# # # 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# # #     *Примеры:*

# # #     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
# # # """


# # # l=[]
# # # a=(int(input('getnumber')))
# # # for i in range(-a,a+1):
# # #     l.append(i)
# # # print(l)


# # # ---------------------------------++++++++++++++++++++++++++++------------------************************


# # # Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.


# # # a=(int(input('getnumber')))
# # # if((a%5==0 and a%10==0) or a%15==0 and a%30!=0 ):
# # #     print ('yes')
# # # else :
# # #     print('no')


# # # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# # # 2. Для натурального n создать словарь индекс-значение, состоящий из 
# # элементов последовательности 3n + 1.
# #     *Пример:*
# #     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Введите число: '))
# myDict = {i: 3*i + 1 for i in range(1, n + 1)}
# print(myDict)


# одинаковы строки

# str1 = input('Введите 1 строку:')
# str2 = input('Введите 2 строку:')
# count = 0
# for ch in str1:
#     if (str2.find(ch) >= 0):
#         count += 1
# print (count)
# n = int(input('Введите число: '))
# myDict = {i: 3*i + 1 for i in range(1, n + 1)}
# print(myDict)
# */*/*/*/*/*/*/*/*/*/*/*/*/**//*///***//////////****
# first_string = input('Введите первую строку: ')
# second_string = input('Введите вторую строку: ')

# a = set(first_string)
# b = set(second_string)

# print(a)
# print(b)

# c = (a & b)

# print(len(c))


# # цуммы цифр
# f = float(input('Введите число: '))
# digitSumm = 0
# fStr = str(f)
# for ch in fStr:
#     if ch != '.' and ch != '-':
#         digitSumm += int(ch)
# print(digitSumm)