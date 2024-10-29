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

# Определяем класс. Указываем, что наследуес класс Car
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        # вызываем конструктор наследуемового класса
        super().__init__(make, model)
        # Дополняем конструктор новым свойством
        self.battery_capacity = battery_capacity

    # Дополняем класс новым методом
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()