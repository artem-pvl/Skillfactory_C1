from geometric_shapes import Rectangle, Square, Circle

if __name__ == '__main__':

    rectangle_1 = Rectangle(5, 10, 50, 100)
    square_1 = Square(10, 10, 30)
    circle_1 = Circle(30, 50, 70)

    print("Rectangle init: " + str(rectangle_1))
    print("Square init: " + str(square_1))
    print("Circle init: " + str(circle_1))

    print(rectangle_1.set_x("a"))
    print(rectangle_1.set_x(10))
    print(rectangle_1.set_x(-10))

    print(rectangle_1)
    print(rectangle_1.get_area())
