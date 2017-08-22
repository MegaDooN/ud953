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

    def __iter__(self):
            return iter(self.coordinates)

    def __getitem__(self,index):
            return self.coordinates[index]

    # Multiply vector by scalar
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
        tolerance = 1e-10
        dot_product = (self * v) / (self.magn() * v.magn())

        if abs(dot_product) - 1.0 < tolerance  and abs(dot_product) > 1.0:
            dot_product = 1.0 if dot_product > 0 else -1.0

        angle_in_radians = numpy.arccos(dot_product)
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

    # parallel projection on vector
    def proj_parallel(self, v):
        return v.norm().mul((self * v.norm())) # (self * v) * v

    # orthogonal projection of vector
    def proj_orthogonal(self, v):
        return self - self.proj_parallel(v)

    # cross vectors
    def cross(self, v):
        x1, y1, z1  = self.coordinates
        x2, y2, z2 = v.coordinates

        x3 = y1 * z2 - y2 * z1
        y3 = - (x1 * z2 - x2 * z1)
        z3 = x1 * y2 - x2 * y1

        return Vector([x3, y3, z3])


    # area of parallelogram
    def area_parallelogram(self, v):
        cross_product = self.cross(v)
        return cross_product.magn()


    # area of trianle
    def area_triangle(self, v):
        return 0.5 * self.area_parallelogram(v)
