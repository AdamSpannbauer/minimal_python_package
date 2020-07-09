def rect_area(w, h):
    """Calc area of a rectangle

    :param w: width of rectangle
    :param h: height of rectangle
    :return: area of rectangle
    """
    return w * h


def square_area(a):
    """Calc area of a square

    :param a: length of square legs
    :return: area of square
    """
    return rect_area(a, a)
