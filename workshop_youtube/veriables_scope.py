#
# #лушче не обьявлять такие пременные которые будут менться в функции
# varible = "It's my live!"
#
# def my_function():
#     varible = "Its not my live!"
#     print(varible)
#
# my_function()
#
#
# print(varible)

# #Лучше использовать так вне скоупа толкьо константы
# COMFORTABLE_TEMPLERATURE = 25
#
# def get_diff_from_comfortable_temp(*, temp: int = COMFORTABLE_TEMPLERATURE) -> int :
#     return  COMFORTABLE_TEMPLERATURE - temp
#
#
# print(get_diff_from_comfortable_temp(temp=25))

# global_var = "I'm a global varible"
#
# def my_function():
#     global  global_var
#     global_var = "I denfined inside inside the scope of my_function"
#
#
# print(global_var)
# my_function()
# print(global_var)



DEFAULT_LEVEL_EXPERIENCE = 200

def is_leveled_up(*, current_experience: int, gained_experience: int) -> bool:
    total_experience = current_experience + gained_experience
    level_up = False

    if total_experience >+ DEFAULT_LEVEL_EXPERIENCE:
        level_up = True

    return  level_up

print(is_leveled_up(current_experience=150, gained_experience= 60))
print(is_leveled_up(current_experience=150, gained_experience= 10))