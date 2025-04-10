# number_1 = [1, 2, 3, 4, 5]
# number_2 = [6, 7, 8, 9, 10]
#
#
# def find_average(numbers):
#     avgerage = sum(numbers) / len(numbers)
#     return avgerage
#
#
# average_1 = find_average(number_1)
# average_2 = find_average(number_2)
# print(average_1, average_2)


#Функция считает колличесво гластный в тексте
# def count_vowels(sting):
#     VOWELS = "aeiouAEIOU"
#     count = 0
#     for char in sting:
#         if char in VOWELS:
#             count += 1
#
#     return count
#
# print(count_vowels("HELLOOOOOO!"))



# def nothing():
# #     pass
# # #заглушка функции


def format_date(*, day: int, month: str) -> str: #тип возвращаемого значения
    return f"The date is {day} of {month}"


print(format_date( day=26 , month="May"))


def custom_greeting(*, name:str, greeting: str = "hello") -> str:
    return  f"{greeting}, {name}"

print(custom_greeting(name="Joen", greeting= "Good morning"))
print(custom_greeting(name="Ilya"))