# fruits = ["apple", "banana","cherry"]
# print(fruits)
#
# print(len(fruits)) #Колличесво элиментов в списке

# random_list = list(("apple", 1, 1.5, True, [1, 2, 3])) # Для нескольких атриубтов в списке нужно использовать(("первое значение" , 2)) или можно использовать []
#
#
# print(False in random_list) #in сравнивает есть ли в списке эта запись
#
# my_list1 = [1, 2, 3]
# my_list2 = [1, 3, 2]
# my_list3 = [1, 2, 3]
#
# print(my_list1 + my_list3)


# print(bool([])) #бул от пустого списка false логика как с str и bool
# print(bool([0 , 2]))


element1 = "apple"
element2 = "banana"
element3 = "cherry"

fruits1 = [element1, element3, element2]
fruits1.append("kivi") #добавлении атрибута в уже существующий список.
#В отличие от строки при добавлении списка изменяется первоначальный список
print(fruits1)
#fruits1.pop() #убирает последнйи атриубт из списка
print(fruits1)
# chart = list(element2) Из строки возьмется каждая буква и внесется в объект списка
# print(chart)

fruits2 = ["fig", "grape"]

fruits2.extend(fruits1) #добавляет список в список

print(fruits2)



