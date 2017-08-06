import vector

print dir(vector)

vector1 = vector.Vector([8.218, -9.341])
vector2 = vector.Vector([-1.129, 2.111])
print vector1 + vector2


vector3 = vector.Vector([7.119, 8.215])
vector4 = vector.Vector([-8.223, 0.878])
print vector3 - vector4


multiplier = 7.41
vector5 = vector.Vector([1.671, -1.012, -0.318])
print vector5.mul(multiplier)
