

class Car:
    def __init__(self, color: str, price: int) -> None:
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        if not isinstance(price, int):
            raise TypeError("Цена должна быть целым числом")

        self.color = color
        self.price = price


    def get_final_price(self, collor: str) -> int:
        """Возвращает обновленную цену"""
        base_price = self.price

        if collor == "red":
            final_price = base_price * 1.15
        else:
            final_price = base_price
        return final_price


class HeavyCar(Car):
    def __init__(self, color: str, price: int, has_triler: bool) -> None:
    # тут мы вызываем конструктор родительского класса
    # и передаем ему параметры
        super().__init__(color, price)
    #добавляем свой параметр
        self.has_triler = has_triler

        if not isinstance(has_triler, bool):
            raise TypeError("has_trailer должен быть булевым значением")

    def get_final_price(self,color:str) -> int:
        """Переопределенный метод:добавляет 25% если есть прицеп"""
        #получаем цену из родиетльского класса
        base_prise = super().get_final_price(color)

        if self.has_triler:
            return int(base_prise * 1.25)
        else:
            return base_prise


my_car =Car(color="red", price=100000)
print(f"My_car is {int(my_car.get_final_price('red'))}!")


heavy_car = HeavyCar("blue", 2000000,  has_triler= False)
print(f"Heavy_cars is {heavy_car.get_final_price('blue')}!")



heavy_car_with_trailer = HeavyCar("black", 2000000, True)
print(f"Heavy_car_with_trailer is {heavy_car_with_trailer.get_final_price('blue')}!")

