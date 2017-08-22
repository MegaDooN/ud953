import vector

v1 = vector.Vector([3.039, 1.879])
v2 = vector.Vector([0.825, 2.036])
print v1.proj_parallel(v2)
print ""


v3 = vector.Vector([-9.88, -3.264, -8.159])
v4 = vector.Vector([-2.155, -9.353, -9.473])
print v3.proj_orthogonal(v4), ""
print ""


v5 = vector.Vector([3.009, -6.172, 3.692, -2.51])
v6 = vector.Vector([6.404, -9.144, 2.759, 8.718])
print v5.proj_parallel(v6)
print v5.proj_orthogonal(v6)
