class Vector(object):
    """docstring for Vector."""
    def __init__(self, coordinates):
        super(Vector, self).__init__()
        try:
            if not coordinates:
                raise ValueError
                pass
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            pass
        except ValueError:
            raise ValueError('The coordinates must be non empty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')
        except Exception as e:
            raise

    def __str__(self):
        return 'Vector {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates);

    def __sub__(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates);

    def mul(self, v):
        new_coordinates = [v * x for x in self.coordinates]
        return Vector(new_coordinates);


vector1 = Vector([8.218, -9.341])
vector2 = Vector([-1.129, 2.111])
print vector1 + vector2


vector3 = Vector([7.119, 8.215])
vector4 = Vector([-8.223, 0.878])
print vector3 - vector4


multiplier = 7.41
vector5 = Vector([1.671, -1.012, -0.318])
print vector5.mul(multiplier)
