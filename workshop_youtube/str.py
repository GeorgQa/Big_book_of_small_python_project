my_str1 ="Hello"
my_str2 = 'Hello'

final_str =  my_str1 == my_str2
print(final_str)

first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " +  last_name
length = len(full_name)
print(length)
print(first_name + " " +  last_name)



my_int = 100
my_string = str(my_int)

print(type(my_string))

my_int2 = 15

bug_int = 2 ** 1000
print(len(str(bug_int)))


#проверка того что в тексте есть это слова. Данный поиск регистрозависимый , а также проверяет bool
String_text = "                  hey, world                "
print("hey" in String_text)
print(len(String_text.upper().strip())) #Стрип убирает лишние пробелы в строке. было 44 стало 23м

print(String_text.replace("hey" , "python")) #replase заменяет в строке
# count подсчитывает колличество в строке
print(String_text.count("l"))


 #пример проверки вводимых данных от пользователя
integer = input("Enter a number: ")
if integer.isdecimal():#проверяет является ли данные строкой
    integer = int(integer)

print(type(integer))


print(f"Можно в строке делать какие то действия например {my_int + my_int2 } либо { my_int * my_int2} ")





string = input("Enter a number: ")
if string.isdecimal():#проверяет является ли данные строкой
    my_integer = int(string)
    print(f" {my_integer} is number")
else:
    print(f" {string} is not a number")