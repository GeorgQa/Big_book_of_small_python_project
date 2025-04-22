fruits = ["apple", "banana","cherry"]

print(fruits[-3])
print(fruits[0])
#Возможный диапазон значений с минус бесконечности до -1 и с 0 до плюс бесконечности

#чтобы поменять местами значение индексов можно использовать данную конструкцию
fruits[0], fruits[2] = fruits[2], fruits[0]


fruits[0] = "pineapple"
print(fruits)


list_int = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list_int = list_int[0:5]
new_full_list_int = list_int[0:len(list_int)]
#Так можно вернуть сразу весь список
#тоже самое но проще
# new_full_list_int = list_int[:]

# new_full_list_int = list_int[: : 2 ] Каждый второй

print(new_list_int)
print(new_full_list_int)


#Можно также сделать слайс из конца в начало

string =  "Hey , dady!"
print(string[::2])