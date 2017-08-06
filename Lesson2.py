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


my_vector = Vector([1,2,3])
print my_vector

my_vector2 = Vector([1,2,3])
my_vector3 = Vector([-1,2,3])

print my_vector == my_vector2
print my_vector == my_vector3
