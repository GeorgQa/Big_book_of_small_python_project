
from workshop_youtube.old_add.sorted_and_filters import sort_by_len

element = [ 1, 23, 343, 4345, 6768, 78922, 890234]


sort_by_len_lambda = lambda  element: len(element)
print("C лямбда", sort_by_len_lambda(element=element))

print("Без лямбды", sort_by_len(element))

