# Определение класса
class Car:
    # Инициализация класса, через конструктор
    def __init__(self, make, model):
        # Установка базовых значений
        self.make = make
        self.model = model

    # Определение метода drive
    def drive(self):
        print(f"Driving the {self.make} {self.model}")


# Создание экземпляра класса
my_car = Car("Toyota", "Corolla")
# Вызов метода drive
my_car.drive()