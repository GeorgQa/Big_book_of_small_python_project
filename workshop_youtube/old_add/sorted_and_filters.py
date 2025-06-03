fruicts_for_sorted =  ["bananna", "kivi", "apple", "cherry", "orange"]

fruicts_for_sorted_data = sorted(fruicts_for_sorted)
print(fruicts_for_sorted_data)

#Та же сортировка только в обратном порядке
fruicts_for_sorted_reverse = sorted(fruicts_for_sorted , reverse=True)
print(fruicts_for_sorted_reverse)

def sort_by_len(element: str)-> int:
    return len(element)

#Передаем в функцию другую функцию, агрументом. Сортируем слова по длине
sorted_function = sorted(fruicts_for_sorted,key=sort_by_len)
print("Слова по длине", sorted_function)

#Пример с массивом
people_from_sort = [
    {"name": "Alice", "age": 21},
    {"name": "Egor", "age": 29},
    {"name": "Geogre", "age": 25},
    {"name": "Anna", "age": 22},
    {"name": "Max", "age": 30},
    {"name": "Olga", "age": 24},
    {"name": "Ivan", "age": 27},
    {"name": "Sophia", "age": 19},
    {"name": "Dmitry", "age": 35},
    {"name": "Elena", "age": 28},
    {"name": "Alex", "age": 31},
    {"name": "Natalia", "age": 26},
    {"name": "Sergey", "age": 33},
    {"name": "Victoria", "age": 23},
    {"name": "Pavel", "age": 32},
    {"name": "Maria", "age": 20},
    {"name": "Artem", "age": 34},
    {"name": "Ksenia", "age": 18},
    {"name": "As", "age": 18}
]
#Достаем значение возраста из персонажей
def sort_dy_person(peorson:dict) -> int:
    return peorson["age"]
#Используем сортировку
sorted_from_people = sorted(people_from_sort, key= sort_dy_person)
print(sorted_from_people)

#Сортировка по 2 признакам

def sort_dy_age_name(element:dict) -> tuple[int, str]:
    return element["age"], element["name"]

sorted_from_age_and_name = sorted(people_from_sort, key=sort_dy_age_name)

print("Sorted by name and age", sorted_from_age_and_name)

def is_even(n: int) -> bool:
    return  n % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,0,11,12,14,15]

filetred_numbers = list(filter(is_even, numbers))
print(filetred_numbers)
print(type(filetred_numbers))


def is_filter_people(perspon: dict) -> bool:
    return perspon["age"] >= 18

filter_of_people = list(filter(is_filter_people, people_from_sort))

print(filter_of_people)
print(type(filter_of_people))
