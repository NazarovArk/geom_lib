def area(a, b):
    '''
    Calculates the area of a rectangle with sides a and b.

        Parameters:
            a (float): rectangle first side
            b (float): rectangle perpendicular to the side

        Returns:
            rectangle_area (float): area of a rectangle with sides a and b
    '''
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("Sides of the rectangle must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Sides of the rectangle must be positive")
    return a * b 

def perimeter(a, b):
    '''
    Calculates the perimeter of a rectangle with sides a and b.

        Parameters:
            a (float): rectangle first side
            b (float): rectangle perpendicular to the side

        Returns:
            rectangle_perimeter (float): perimeter of a rectangle with sides a and b
    '''
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("Sides of the rectangle must be numbers")
    if a < 0 or b < 0:
        raise ValueError("Sides of the rectangle must be positive")
    return 2 * (a + b)
