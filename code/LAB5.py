class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# создаем экземпляры классов с фигурами
newCircle_1 = Circle(5)
newCircle_2 = Circle(25)

newRectangle_1 = Rectangle(5, 4)
newRectangle_2 = Rectangle(10, 12)
# кладем в массив
figures = [newCircle_1, newCircle_2, newRectangle_1, newRectangle_2]
# обращаемся к каждому элементу массива и вызываем метод area()
for figures in figures:
    print(figures.area())
