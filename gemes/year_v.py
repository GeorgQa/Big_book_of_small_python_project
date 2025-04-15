# import sys
#
# if True:
#     print("Чет там")
#
# #Все что внутри if выполняеется только есть условие == True
# if False:
#     print("Где-то там")
#
# x = 1
# #если увдолетворяет сразу 2 условиям то пойдет в перовое
# if x > 0:
#     print("x is positive")
# elif x < 0:
#     print("x is neative")
# else:
#     print("x is zero")


# x = 10
# y = 20
# if  x > 0:
#     if y > 0:
#         print("x and y are postive")
# ниже приведен пример он более правильный

# x = -1
# y = 20
# if  x > 0 and y > 0:
#         print("x and y are postive")
# else:
#     print("x or y negative")
#
# message = "67767"
# if message:# Можно не прописывать bool(message)
#     print("message os not empty")

print("Введите год:")
year_v = int(input("> "))
if year_v == "":
    sys.exit()

if not year_v % 4 and year_v % 100 != 0:
    print("Year is leap!")
elif not year_v % 400:
    print("Year is leap!")
else:
    print("Year is not leap!")

#Вариант без изменений
# year_v = int(year_v)
#
# if year_v % 4 == 0 and year_v % 100 != 0:
#     print("Year is leap!")
# elif year_v % 400 == 0:
#     print("Year is leap!")
# else:
#     print("Year is not leap!")