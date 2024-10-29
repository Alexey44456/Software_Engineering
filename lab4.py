# Определение класса
class Car:
    # Инициализация класса, через конструктор
    def __init__(self, make, model):
        self._make = make # Защищённый атрибут
        self.__model = model # Приватный атрибут

    # Определение метода drive
    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("Toyota", "Corolla")
print(my_car._make) # Выводим защищённый атрибут
my_car.drive()
