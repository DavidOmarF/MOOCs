import math

def polysum (n, s):
    '''
        n: int; number of sides of a regular polygon
        s: int or float; lenght of each side of polygon

        returns: area plus squared perimeter of the polygon
    '''
    def area (n, s):
        '''
            n: int
            s: int or float

            returns: area of a regular polygon with n sides and side length s
        '''
        return (0.25 * n * s**2) / math.tan(math.pi/n)
    def perimeter(n, s):
        '''
            n: int
            s: int or float

            returns: perimeter of a regualr polygon with n sides and side length s
        '''
        return n * s
    return round((area(n, s) + perimeter(n, s) ** 2), 4)