flat_number = input("Введите номер квартиры:")
if flat_number.isdecimal():
    flat_number = int(flat_number)
else:
    print("Введите пожалуйста число ")

enterance_number = flat_number  // 20
flor_number = flat_number  % 20 // 4

print(f"Квартира находиться в {enterance_number} подъезде")
print(f"квартира находиться на {flor_number} этаже")
