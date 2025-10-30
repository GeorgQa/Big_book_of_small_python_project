# Родительский класс "летающий"
class Flyable:
    def fly(self):
        return "Я умею летать!"


# Родительский класс "плавающий"
class Swimmable:
    def swim(self):
        return "Я умею плавать!"


# Дочерний класс, наследующий от обоих
class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Привет, я утка по имени {self.name}!"


# Использование
donald = Duck("Дональд")

print(donald.introduce())  # Привет, я утка по имени Дональд!
print(donald.fly())        # Я умею летать!
print(donald.swim())       # Я умею плавать!