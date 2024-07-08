import functools


class Shape(object):

    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def __str__(self):
        return "Shape " + self.name + ": {}"

    def __eq__(self, other):
        return abs(self.area() - other.area()) <= 0.01

    def __lt__(self, other):
        # print("I am called when sorted by defaul")
        if self == other:
            return self.perimeter() < other.perimeter()
        return self.area() < other.area()

    def __gt__(self, other):
        if self == other:
            return self.perimeter() > other.perimeter()
        return self.area() > other.area()


class Rectangle(Shape):

    def __init__(self, side1=0, side2=0, name=""):
        Shape.__init__(self, name)
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2 * (self.side1 + self.side2)

    def __str__(self):
        return "Rectangle {}: {{area={}, peri={}}}".format(self.name, self.area(), self.perimeter())


class Square(Rectangle):

    def __init__(self, side=0, name=""):
        Rectangle.__init__(self, side, side, name)

    def __str__(self):
        return "Square {}: [area={}, peri={}]".format(self.name, self.area(), self.perimeter())


class Circle(Shape):
    PI = 3.1415

    def __init__(self, radius=0, name=""):
        Shape.__init__(self, name)
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2

    def perimeter(self):
        return Circle.PI * self.radius * 2

    def __str__(self):
        return "Circle {}: (area={}, peri={})".format(self.name, self.area(), self.perimeter())


# c = Circle(4, "cir")
# r = Rectangle(7, 5, "rec")
# s = Square(6, "sqr")
#
# print(c)
# print(r)
# print(s)
#
# shapes = [c, r, s]
# for shape in shapes:
#     print(shape)
#
# shapes.sort()
#
# for shape in shapes:
#     print(shape)


# c, r, s = Circle(5), Rectangle(3, 4), Square(3)
# print(c)
# print(r)
# print(s)


# r1 = Rectangle(9, 4)
# r2 = Rectangle(6, 6)
# recs = [r1, r2]
# for rec in recs:print(rec)
# # recs.sort(key=functools.cmp_to_key(Rectangle.__gt__))
# recs.sort(reverse=True)
# for rec in recs:print(rec)


## A NOTE IMPORTANT
# def comp(x, y):
#     return x > y
#
# l = [1, 2, 3]
# python 3 has removed cmp attribute to key attribute
# l.sort(cmp=comp)
# l.sort(key=functools.cmp_to_key(comp))


