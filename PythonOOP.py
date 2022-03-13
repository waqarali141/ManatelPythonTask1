from math import pi


class Circle:
    def __init__(self, radius: float):
        """
        Initialize the circle class
        :param radius: radius of the circle
        """
        self.radius = radius

    def get_area(self) -> float:
        """
        calculate the radius of the circle
        :return: radius rounded to two decimal
        """
        return round(pi * self.radius ** 2, 2)

    def get_perimeter(self) -> float:
        """
        calculate the perimeter of the circle
        :return: perimeter rounded to two decimal
        """
        return round(2 * pi * self.radius, 2)


if __name__ == "__main__":
    c = Circle(radius=10)
    print("Radius of the circle: {}, Perimeter of the circle: {}".format(c.get_area(), c.get_perimeter()))

