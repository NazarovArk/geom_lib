import math


def area(r):
    '''
    Calculates the area of ​​a circle with radius r.

        Parameters:
            r (float): circle radius

        Returns:
            cirsle_area (float): area of ​​a circle with radius r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Calculates the perimeter of ​​a circle with radius r.

        Parameters:
            r (float): circle radius

        Returns:
            cirsle_perimeter (float): perimeter of ​​a circle with radius r
    '''
    return 2 * math.pi * r

