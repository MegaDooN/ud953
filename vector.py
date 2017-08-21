import math, numpy

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

    def __mul__(self, v):
        new_coordinates = [x*y for x,y in zip(self.coordinates, v.coordinates)]
        return sum(new_coordinates);

    def mul(self, v):
        new_coordinates = [v * x for x in self.coordinates]
        return Vector(new_coordinates);

    def magn(self):
        v = 0
        for x in self.coordinates:
            v += x*x
        return math.sqrt(v)

    def norm(self):
        return self.mul(1./self.magn())

    def angle_with(self, v, in_radians = True):
        angle_in_radians = numpy.arccos( (self * v) / (self.magn() * v.magn()) )
        return angle_in_radians if in_radians else angle_in_radians / numpy.pi * 180.

    def is_zero(self, tolerance = 1e-10):
        return self.magn() < tolerance

    def is_orthogonal_to(self, v, tolerance = 1e-10):
        return numpy.abs(self * v) < tolerance

    def is_parallel_to(self, v):
        return (self.is_zero() or
                v.is_zero() or
                0 == self.angle_with(v) or
                numpy.pi == self.angle_with(v))
