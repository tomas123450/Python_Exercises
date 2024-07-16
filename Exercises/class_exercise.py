class AreaSquare:
    color = "Blue"  # class variable

    def __init__(self, l, h) -> None:
        self.l = l  # instance variables
        self.h = h  #

    def calculate_area(self):  # metodas
        return self.l * self.h

    def print_area(self):
        print(f"The area of square is {self.calculate_area()}")


# Inheritance
class Parent:
    def __init__(self) -> None:
        print("Hello world")

    def parent_method(self):
        print("parent_method")


class ChildClass(Parent):  # inherited class (randomfun will be accesable)
    def __init__(self) -> None:
        pass


# Multiple inheritance

"""Method resolution order MRO Method Resolution Order (MRO) -
# Search is done first in current class, then
# the search continues into parent classes in depth-first,
left-right fashion without searching the same class twice
"""


class Cars:
    def noise(self):
        print("beep")


class Bmw:
    def get_price(self):
        print("price")


class Ford(Cars, Bmw):
    pass


def main():
    area1 = AreaSquare(10, 5)
    area1.print_area()

    p = Parent().parent_method()
    c = ChildClass().parent_method()

    car = Cars()
    print(Cars.mro())


if __name__ == "__main__":
    main()
