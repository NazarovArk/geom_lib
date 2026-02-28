import math


def area(r):
    '''
    Calculates the area of a circle with radius r.

        Parameters:
            r (float): circle radius

        Returns:
            cirsle_area (float): area of a circle with radius r
    '''
    if type(r) not in [int, float]:
        raise TypeError('Radius must be a number')
    if r < 0:
        raise ValueError('Radius must be non-negative')
    return math.pi * r * r


def perimeter(r):
    '''
    Calculates the perimeter of a circle with radius r.

        Parameters:
            r (float): circle radius

        Returns:
            cirsle_perimeter (float): perimeter of a circle with radius r
    '''
    if type(r) not in [int, float]:
        raise TypeError('Radius must be a number')
    if r < 0:
        raise ValueError('Radius must be non-negative')
    return 2 * math.pi * r

