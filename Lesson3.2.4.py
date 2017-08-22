from vector import Vector
from line import Line
from decimal import Decimal


def show_results(l1, l2):
    if l1.is_parallel_to(l2):
        print 'Are parallel'
        if l1.is_similar_to(l2):
            print ' and are similar'
    else:
        print "Intersect in: "
        print l1.intersection_with(l2)


line1 = Line(normal_vector = Vector([4.046, 2.836]), constant_term = 1.21)
line2 = Line(normal_vector = Vector([10.115, 7.09]), constant_term = 3.025)
print 'Line 1 vs Line 2:'
show_results(line1, line2)
print ""


line3 = Line(normal_vector = Vector([7.204, 3.182]), constant_term = 8.68)
line4 = Line(normal_vector = Vector([8.172, 4.114]), constant_term = 9.883)
print 'Line 3 vs Line 4:'
show_results(line3, line4)
print ""


line5 = Line(normal_vector = Vector([1.182, 5.562]), constant_term = 6.744)
line6 = Line(normal_vector = Vector([1.773, 8.343]), constant_term = 9.525)
print 'Line 5 vs Line 6:'
show_results(line5, line6)
print ""
