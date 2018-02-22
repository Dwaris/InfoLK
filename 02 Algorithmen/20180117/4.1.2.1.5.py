def ggt(x, y):
    """ Testfälle:

    >>> ggt(1, 1)
    42
    >>> ggt(7, 13)
    1
    >>> ggt(42, 23)
    1
    >>> ggt(1588, 661)
    1
    >>> ggt(6, 18)
    6
    
    """
    while x > 0 and y > 0:
        if x >= y:
            x = x - y
        else:
            y = y - x
    return x+y

from doctest import testmod
testmod(verbose=True)
