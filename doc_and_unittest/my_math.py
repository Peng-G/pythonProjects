def square(x):
    """
    >>> square(2)
    4
    >>> square(3)
    9
    """
    return x*x


def product(x, y) -> any:
    return x*y


if __name__ == '__main__':
    import doctest, my_math
    doctest.testmod(my_math)
