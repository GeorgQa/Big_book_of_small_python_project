people = [
    {"name": "Alice", "age": 25},
    {"name": "Joen", "age": 29},
    {"name": "Kate", "age": 22},
    {"name": "Kate", "age": 22},
    {"name": "Name", "age": 23},
]
def sorted_by_age(person:dict) -> int:
    return person["age"]

def sort_by_age_name(element:dict) -> tuple[int, str]:
    return element["age"],element["name"]


def anti_sort_by_age_name(element:dict) -> tuple[int, str]:
    return sorted(element["age"],element["name"], reverse=True)

sorted_people = sorted(people, key=anti_sort_by_age_name)
print(sorted_people)