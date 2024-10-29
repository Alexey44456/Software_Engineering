# Определение класса
class Car:
    # Инициализация класса, через конструктор
    def __init__(self, make, model):
        # Установка базовых значений
        self.make = make
        self.model = model

# Создание экземпляра класса
my_car = Car("Toyota", "Corolla")