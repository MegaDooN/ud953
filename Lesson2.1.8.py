import vector, numpy

v1 = vector.Vector([7.887, 4.138])
v2 = vector.Vector([-8.802, 6.776])
print v1*v2

v3 = vector.Vector([-5.955, -4.904, -1.874])
v4 = vector.Vector([-4.496, -8.755, 7.103])
print v3*v4

v5 = vector.Vector([3.183, -7.627])
v6 = vector.Vector([-2.668, 5.319])
print numpy.arccos( v5 * v6 / ( v5.magn() * v6.magn() ) )

v7 = vector.Vector([7.35, 0.221, 5.188])
v8 = vector.Vector([2.751, 8.259, 3.985])
print numpy.arccos( v7 * v8 / ( v7.magn() * v8.magn() ) ) / numpy.pi * 180

