import vector

v1 = vector.Vector([-7.579, -7.88])
v2 = vector.Vector([22.737, 23.64])
print v1.is_parallel_to(v2)
print v1.is_orthogonal_to(v2)
print ""

v3 = vector.Vector([-2.029, 9.97, 4.172])
v4 = vector.Vector([-9.231, -6.639, -7.245])
print v3.is_parallel_to(v4)
print v3.is_orthogonal_to(v4)
print ""

v5 = vector.Vector([-2.328, -7.284, -1.214])
v6 = vector.Vector([-1.821, 1.072, -2.94])
print v5.is_parallel_to(v6)
print v5.is_orthogonal_to(v6)
print ""

v7 = vector.Vector([2.118, 4.827])
v8 = vector.Vector([0, 0])
print v7.is_parallel_to(v8)
print v7.is_orthogonal_to(v8)
print ""
