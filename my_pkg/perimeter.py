def rect_perimeter(w, h):
    """Calc perimeter of a rectangle

    :param w: width of rectangle
    :param h: height of rectangle
    :return: perimeter of rectangle
    """
    return w * 2 + h * 2


def square_perimeter(a):
    """Calc perimeter of a square

    :param a: length of square legs
    :return: perimeter of square
    """
    return rect_perimeter(a, a)
