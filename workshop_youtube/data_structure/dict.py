# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }


person = {}

person["job"] = "Engineer"
person["age"] = 30
person["city"] = "New York"


# print(person.get("job" , "USA"))
# print(person.get("name" , "Jack"))



# for item in person.items():
#     key, value = item
#     print(key)
#     print(value)
#     print(type(item))

#Сравнение словарей

other_person = {
    "job":"Engineer",
    "city": "New York",
    "age": 30
}

additional_person_info = {
    "job":"Plotnik",
    "city": "New York",
    "age": 30,
    "country": "USA"
}

person = person | additional_person_info

print(person)
