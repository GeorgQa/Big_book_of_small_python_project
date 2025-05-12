
def add_all(*args):
    summary = 0
    for num in args:
        summary += num
    return summary

print(add_all(1,2,3,4,5))



values = [1,2,3,4,5]
other_valyes = [6,7,8,9,10]

print(add_all(*values, *other_valyes))



def introduce(**kwargs):
    print(kwargs)
    print(type(kwargs))

introduce(name = "John", age =30 , city = "New Your")




def modify_dict(old_dict: dict, **kwargs) -> tuple[dict,bool]:
        is_modifyed = False

        for key, value in kwargs.items():
            if old_dict.get(key) != value:
                old_dict[key] = value
                is_modifyed = True
        return old_dict,is_modifyed



product = {'id': 1, 'name':'Laptop', 'price': 999.99}

structure = modify_dict(old_dict=product, name = "Laptop")

print(structure)
print(type(structure))

