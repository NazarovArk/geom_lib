def area(a, h):
    '''
    Calculates the area of a triangle with side a and height h.

        Parameters:
            a (float): triangle first side
            h (float): triangle height perpendicular to first side

        Returns:
            triangle_area (float): area of a triangle
    '''
    if type(a) not in [int, float] or type(h) not in [int, float]:
        raise TypeError("Side and height of a triangle must be numbers")
    if a < 0 or h < 0:
        raise ValueError("Side and height of a triangle must be positive")
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Calculates the perimeter of a triangle with sides a, b, c.

        Parameters:
            a (float): first triangle side
            b (float): second triangle side
            c (float): third triangle side

        Returns:
            triangle_perimeter (float): perimeter of a triangle
    '''
    if type(a) not in [int, float] or type(b) not in [int, float] or type(c) not in [int, float]:
        raise TypeError("Sides of a triangle must be numbers")
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Sides of a triangle must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Triangle with such sides does not exist")
    return a + b + c
