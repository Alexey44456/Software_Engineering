class Animal():
    # Инициализация полей
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Метод для вывода информации о животном
    def who_am_i(self):
        print(f"Меня зовут {self.name}, и я {self.species}")

class Dog(Animal):
    def __init__(self, name, breed, energy):
        # вызываем конструктор наследуемого класса
        super().__init__(name, "Собака")
        # Дополняем конструктор новыми свойствами
        self._breed = breed  # Защищённое свойство
        self._energy = energy  # Защищённое свойство

        self.__playtime = 0  # Приватное свойство

    def bark(self):

        print(f"{self.name} говорит: Гав!")

    def play(self, time):
        self.__playtime += time
        self._energy -= time * 5  # Энергия уменьшается с каждой игрой
        print(f"{self.name} играл(а) {time} минут. Общее время игры: {self.__playtime} минут.")

    def check_energy(self):
        print(f"Энергия {self.name}: {self._energy}")

# Создаем экземпляр класса Dog
dog = Dog("Бадди", "Золотистый ретривер", 100)

dog.who_am_i()

dog.check_energy()

dog.bark()

dog.play(10)
dog.play(15)

dog.check_energy()