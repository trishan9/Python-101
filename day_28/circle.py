from shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle", radius, radius)

    def area(self):
        return 3.14 * super().area()


a = Shape("Square", 10, 10)
print(a.area())
print(a)
a()
print(a.__repr__())

b = Circle(10)
print(b.area())
print(b)
b()
