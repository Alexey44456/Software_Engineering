class Animal():
    # Инициализация полей
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Метод для вывода информации о животном
    def who_am_i(self):
        print(f"Меня зовут {self.name}, и я {self.species}")

dog = Animal("Бадди", "Золотистый ретривер")
dog.who_am_i()