import math

# homework implement divide remainder: HOW????
# looks like dividing with scalar, not vector

class Vector():
    '''The Vector class represents two values as a vector,
       allows for many math calculations'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, oOther):
        if not isinstance(oOther, Vector):
            raise TypeError('Second object must be a Vector')
        return Vector(self.x + oOther.x, self.y + oOther.y)

    def __sub__(self, oOther):
        if not isinstance(oOther, Vector):
            raise TypeError('Second object must be a Vector')
        return Vector(self.x - oOther.x, self.y - oOther.y)

    def __mul__(self, oOther):
        if isinstance(oOther, Vector):
            return Vector((self.x * oOther.x), (self.y * oOther.y))
        elif isinstance(oOther, (int, float)):
            return Vector((self.x * oOther), (self.y * oOther))
        else:
            raise TypeError('Second value must be a vector or scalar')

    def __abs__(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def __eq__(self, oOther):
        assert_type_vector(oOther)
        return (self.x == oOther.x) and (self.y == oOther.y)

    def __ne__(self, oOther):
        assert_type_vector(oOther)
        return not (self == oOther)

    def __lt__(self, oOther):
        assert_type_vector(oOther)
        if abs(self) < abs(oOther):
            return True
        else:
            return False

    def __gt__(self, oOther):
        assert_type_vector(oOther)
        if abs(self) > abs(oOther):
            return True
        else:
            return False

    # WARNING: These are not actual vector math implementation, just some undefined behavior
    def __truediv__(self, number: float):
        return Vector(self.x / number, self.y / number)

    def __floordiv__(self, number: float):
        return Vector(self.x // number, self.y // number)

    def __mod__(self, number: float):
        return Vector(self.x % number, self.y % number)

    def __str__(self):
        return f'({self.x}, {self.y})'


def assert_type_vector(vector):
    assert isinstance(vector, Vector), 'Value must be a Vector'