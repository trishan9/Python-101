class Shape:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def __call__(self):
        print("This object is callable")

    def __str__(self):
        return f"This object is for the shape {self.name}, str"

    def __repr__(self):
        return f"This object is for the shape {self.name}, repr"


def greet():
    print("Hello World")


if __name__ == "__main__":
    greet()
