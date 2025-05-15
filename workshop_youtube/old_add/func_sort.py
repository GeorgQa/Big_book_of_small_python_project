fructs = ["banana","kiwi","apple"]



longers_world = max(fructs, key=lambda element: len(element))
sorted_fruct = sorted(fructs)

print(sorted_fruct)



def sort_by_len(element:str ) -> int:
    return  len(element)


sort_by_len_lambda = lambda  element: len(element)

print(sort_by_len_lambda("apple"))
print(sort_by_len("apple"))

