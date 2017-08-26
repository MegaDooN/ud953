from vector import Vector
from plane import Plane
from decimal import Decimal


def show_results(p1, p2):
    if p1.is_parallel_to(p2):
        print 'Are parallel'
        if p1.is_similar_to(p2):
            print ' and are similar'
    else:
        print 'Planes are not parallel'

plane1 = Plane(normal_vector = Vector([-0.412, 3.806, 0.728]), constant_term = -3.46)
plane2 = Plane(normal_vector = Vector([1.03, -9.515, -1.82]), constant_term = 8.65)
print 'Plane 1 vs Plane 2:'
show_results(plane1, plane2)
print ""


plane3 = Plane(normal_vector = Vector([2.611, 5.528, 0.283]), constant_term = 4.6)
plane4 = Plane(normal_vector = Vector([7.715, 8.306, 5.342]), constant_term = 3.76)
print 'Plane 3 vs Plane 4:'
show_results(plane3, plane4)
print ""


plane5 = Plane(normal_vector = Vector([-7.926, 8.625, -7.212]), constant_term = -7.952)
plane6 = Plane(normal_vector = Vector([-2.642, 2.875, -2.404]), constant_term = -2.443)
print 'Plane 5 vs Plane 6:'
show_results(plane5, plane6)
print ""
