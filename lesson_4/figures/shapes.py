from abc import ABCMeta, abstractmethod
from math import sqrt, acos, degrees, pi


class Vertex():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape():
    __metaclass__ = ABCMeta

    def __init__(self, verticies):
        self.verticies = verticies

    def edges(self):
        edges_ = []
        for i in range(1, len(self.verticies)):
            edges_.append(sqrt(
                (self.verticies[i].x - self.verticies[i - 1].x)**2
                + (self.verticies[i].y - self.verticies[i - 1].y)**2
            ))
        edges_.append(sqrt(
            (self.verticies[0].x
                - self.verticies[len(self.verticies) - 1].x)**2
            + (self.verticies[0].y
                - self.verticies[len(self.verticies) - 1].y)**2
        ))
        return edges_

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, verticies):
        if len(verticies) != 3:
            raise RuntimeError("Triangle must have 3 verticies")
        Shape.__init__(self, verticies)

    def angles(self):
        a_edge, b_edge, c_edge = self.edges()
        return (
            acos((b_edge**2 + c_edge**2 - a_edge**2) / (2 * b_edge * c_edge)),
            acos((a_edge**2 + c_edge**2 - b_edge**2) / (2 * a_edge * c_edge)),
            acos((a_edge**2 + b_edge**2 - c_edge**2) / (2 * a_edge * b_edge))
        )

    def area(self):
        edges = self.edges()
        half_perimeter = sum(edges) / 2
        return sqrt(
            half_perimeter
            * (half_perimeter - edges[0])
            * (half_perimeter - edges[1])
            * (half_perimeter - edges[2])
        )

    def perimeter(self):
        return sum(self.edges())


class Triangle3D(Triangle):
    def __init__(self, verticies, height):
        """Three verticies and height of figure"""
        Triangle.__init__(self, verticies)
        self.height = height

    def volume(self):
        return self.area() * self.height

    def surface_area(self):
        edges = self.edges()
        areas = [self.area() * 2]
        areas += [edge * self.height for edge in edges]
        return sum(areas)


class Rectangle(Shape):
    def __init__(self, verticies):
        if len(verticies) != 4:
            raise RuntimeError("Rectangle must have 4 verticies")
        Shape.__init__(self, verticies)

    def is_quad(self):
        a_edge, b_edge, c_edge, d_edge = self.edges()
        if a_edge == b_edge and b_edge == c_edge and c_edge == d_edge:
            return True
        return False

    def area(self):
        edges = self.edges()
        return edges[0] * edges[1]

    def perimeter(self):
        return sum(self.edges())


class RectangularCuboid(Rectangle):
    def __init__(self, verticies, height):
        Rectangle.__init__(self, verticies)
        self.height = height

    def volume(self):
        return self.area() * self.height

    def surface_area(self):
        edges = self.edges()
        areas = [self.area() * 2]
        areas += [edge * self.height for edge in edges]
        return sum(areas)


class Circle(Shape):
    def __init__(self, center, radius):
        Shape.__init__(self, center)
        self.radius = radius

    def area(self):
        return self.radius**2 * pi

    def perimeter(self):
        return self.radius * 2 * pi


class Cylinder(Circle):
    def __init__(self, center, radius, height):
        Circle.__init__(self, center, radius)
        self.height = height

    def volume(self):
        return self.area() * self.height

    def surface_area(self):
        return self.perimeter() * self.height + self.area() * 2


if __name__ == "__main__":
    rect_verticies = (
        Vertex(0, 0),
        Vertex(0, 2),
        Vertex(1, 2),
        Vertex(1, 0)
        )
    rect_verticies1 = (
        Vertex(0, 0),
        Vertex(0, 1),
        Vertex(1, 1),
        Vertex(1, 0)
    )
    tr_veticies = (
        Vertex(0, 0),
        Vertex(0, 4),
        Vertex(2, 0)
    )

    tr = Triangle(tr_veticies)
    for angle in tr.angles():
        print degrees(angle), "degrees"
    print tr.area()
    print tr.perimeter()

    rect = Rectangle(rect_verticies1)
    print rect.is_quad()
    print rect.area()
    print rect.perimeter()
    rect1 = Rectangle(rect_verticies)
    print rect1.is_quad()
    print rect1.area()
    print rect1.perimeter()

    c = Circle(Vertex(0, 0), 10)
    print c.area()
    print c.perimeter()

    c3 = Cylinder(Vertex(0, 0), 100, 10)
    print c3.surface_area()
    print c3.volume()

    rect3d = RectangularCuboid(rect_verticies, 10)
    print rect3d.volume()
    print rect3d.surface_area()

    tr3d = Triangle3D(tr_veticies, 10)
    print tr3d.surface_area()
    print tr3d.volume()
