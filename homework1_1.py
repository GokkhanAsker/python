# # Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# # Пример:

# # - 6 -> да
# # - 7 -> да
# # - 1 -> нет
# понедельник = 1
# втокник = 2
# среда = 3
# четверг = 4
# пятница = 5
# суббота = 6
# воскресенье = 7
# x = int(input('Введите число от 1 до 7\n'))
# if x != 1 and x != 2 and x != 3 and x != 4 and x != 5 and x != 6 and x != 7:
#     print('Введите число от 1 до 7 !!!!!!!')
# else:
#     if x == 6 or x == 7:
#         print('да')
#     else:
#         print('нет')


# # ----------------------------------------------------------------------------------------------------------

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Введите значение X, не равное нулю \n'))
# y = int(input('Введите значение Y, не равное нулю \n'))
# if x==0 or y==0:
#     print('не корректное значение попробуйте ещё раз!')
# else:
#     if x > 0 and y > 0:
#         print("первая четверть")
#     elif x < 0 and y > 0:
#         print("вторая четверть")
#     elif x < 0 and y < 0:
#         print("третья четверть")
#     else:
#         print("четвертая четверть")

# # /*--------------------------------------------------------------------------------------------------
# # Напишите программу, которая по заданному номеру четверти,
# # показывает диапазон возможных координат точек в этой четверти (x и y).

# a = int(input('напишите четверт от 1 до 4:\n'))
# if a<1 or a>=5:
#     print('не корректное значение попробуйте ещё раз!')
# else:
#     if a == 1:
#         print('x > 0 and y > 0')
#     elif a == 2:
#         print('x < 0 and y > 0')
#     elif a == 3:
#         print('x < 0 and y < 0')
#     else:
#         print('x > 0 and y < 0')

# # --------------------************-----------------------------****************-----------------------------
# # Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# # Пример:

# # - A (3,6); B (2,1) -> 5,09
# # - A (7,-5); B (1,-1) -> 7,21

# import math

# a1=int(input('Координаты первой точки a1:\n'))
# b1=int(input('Координаты первой точки b1:\n'))
# a2=int(input('Координаты второй точки a2:\n'))
# b2=int(input('Координаты второй точки b2:\n'))
# ab=math.sqrt(math.pow(a2-a1,2)+math.pow(b2-b1,2))
# print('{:.3f}'.format(ab))
# print(ab)