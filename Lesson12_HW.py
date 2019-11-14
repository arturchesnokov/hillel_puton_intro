class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Pi*r**2
    def area(self):
        return 3.1415926535 * self.radius ** 2

    # 2*Pi*r
    def perimeter(self):
        return 2 * 3.1415926535 * self.radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # площадь теугольника по формуле Герона
    def area(self):
        p = self.perimeter() * 0.5
        return (p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


if __name__ == '__main__':
    # Circles check
    c1 = Circle(5)
    c2 = Circle(0)
    c3 = Circle(6.5)
    assert (round(c1.area(), 2) == 78.54)
    assert (round(c2.area(), 2) == 0)
    assert (round(c3.area(), 2) == 132.73)
    assert (round(c1.perimeter(), 2) == 31.42)
    assert (round(c2.perimeter(), 2) == 0)
    assert (round(c3.perimeter(), 2) == 40.84)

    # Rectangles check
    r1 = Rectangle(0, 0)
    r2 = Rectangle(4, 5)
    r3 = Rectangle(2.5, 3.5)
    assert (r1.area() == 0)
    assert (r2.area() == 20)
    assert (r3.area() == 8.75)
    assert (r1.perimeter() == 0)
    assert (r2.perimeter() == 18)
    assert (r3.perimeter() == 12)

    # Triangles check
    t1 = Triangle(0, 0, 0)
    t2 = Triangle(2, 2, 2)
    t3 = Triangle(2.5, 3.4, 3)
    assert (round(t1.area(), 2) == 0)
    assert (round(t2.area(), 2) == 1.73)
    assert (round(t3.area(), 2) == 3.63)
    assert (round(t1.perimeter(), 2) == 0)
    assert (round(t2.perimeter(), 2) == 6)
    assert (round(t3.perimeter(), 2) == 8.9)
