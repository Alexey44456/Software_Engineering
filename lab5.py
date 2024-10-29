# Шаблон, который обязует реализовывать метод area
# По сути это абстрактный класс, который служит лишь шаблоном
class Shape:
    def area(self):
        pass

# Определение класса квадрата
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Переопределения метода area
    def area(self):
        return self.width * self.height
    
# Определение класса круга
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    # Переопределения метода area
    def area(self):
        return 3.14 * self.radius * self.radius
    
rect = Rectangle(20, 40)
print(f"Площадь квадрата: {rect.area()}")

circle = Circle(5)
print(f"Площадь круга: {circle.area()}")