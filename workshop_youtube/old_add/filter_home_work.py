
people = [
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 20},
    {"name": "Bob", "age": 20},
    {"name": "Diana", "age": 30},
]

min_sort_perople = min(people, key=lambda x:(x["age"], -len(x["name"])))

print(min_sort_perople)