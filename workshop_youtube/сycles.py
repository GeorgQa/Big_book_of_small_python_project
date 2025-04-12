





# file_names = ["document1.txt", "image1.jpg", "document2.txt", "image2.jpg" ]
#
#
# #перебираем значения словаря и выводим в новой строке
# for fale_name in file_names:
#     print(fale_name)
#
# #выводим в стоблец по буквам  строку
# greeting = "hello, word!"
# count_0 = 0
# for char in greeting:
#     if char == "o":
#         count_0 += 1
#         print(char)
# print(count_0)

# Синтаксический сахар
# добавить одно в другое
# count = count + 1
# count += 1
# вычесть
# count = count - 1
# count -= 1
# перемножить
# count = count * 2
# count *= 2
# Возвести в степень
# count = 2
# count = count ** 5
# count **= 5


students = ["Alice", "Bob", "charlie", "David" ]
for student in students:
    print(student)
    for char in student:
        print(char)

#
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# #мой вариант
# for number in numbers[::2]:
#     print(number)
#
# #варинат с continue и break
#
# for num in numbers:
#     # if num % 2 == 0 :
#     #     continue
#     # print(num)
#     if num == 10:
#         break
#     print(num)
#
# numbers = [10, 11, 12, 13,14,15]
#
# for i in range(len(numbers)):
#     numbers[i]+= 1
# print(numbers)
#
#
#
# greeting = "hello, world !"
#
# indexes = []
# count = 0
#
# for i in range(len(greeting)):
#    if greeting[i] == "o":
#        count += 1
#        indexes.append(i)
#
# print(indexes)
# print(count)