
def area(a):
    '''
    Calculates the area of a square with side a.

        Parameters:
            a (float): square side

        Returns:
            square_area (float): area of a square with side a
    '''
    if type(a) not in [int, float]:
        raise TypeError("Side of a square must be a number")
    if a < 0:
        raise ValueError("Side of the square must be positive")
    return a * a


def perimeter(a):
    '''
    Calculates the perimeter of a square with side a.

        Parameters:
            a (float): square side

        Returns:
            square_perimeter (float): perimeter of a square with side a
    '''
    if type(a) not in [int, float]:
        raise TypeError("Side of a square must be a number")
    if a < 0:
        raise ValueError("Side of the square must be positive")
    return 4 * a
