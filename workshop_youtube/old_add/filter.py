

def is_event(n:int) -> bool:
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5, 6.7, 8, 9]

filted_numbers = list(filter(is_event, numbers))
print(filted_numbers)
print(type(filted_numbers))