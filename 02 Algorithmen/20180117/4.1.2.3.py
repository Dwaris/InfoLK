def prim(n):

    """ Testfälle:

    >>> prim(1)
    False
    >>> prim(13)
    True
    >>> prim(42)
    False
    """
    prim = True
    if n == 1:
        prim = False
    else:
        i = 2
        while i <= n-1:
            if n % i == 0:
                prim = False
        i += 1    
    return prim
from doctest import testmod
testmod(verbose=True)
