# if True:
#     print("Чет там")
#
# #Все что внутри if выполняеется только есть условие == True
# if False:
#     print("Где-то там")
from gemes.bitMapMessage import message

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

x = -1
y = 20
if  x > 0 and y > 0:
        print("x and y are postive")
else:
    print("x or y negative")

text = "textvrfergf"
if text:
    print("massage is not empty")