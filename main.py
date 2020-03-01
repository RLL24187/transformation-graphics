from display import *
from draw import *
from parsefile import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# translate = make_translate(10, 10, 10)
# print("translation matrix")
# print_matrix(translate)
#
# scale = make_scale(5, 5, 5)
# print("scale matrix")
# print_matrix(scale)
#
# rotX = make_rotX(60)
# print("rotX matrix")
# print_matrix(rotX)
# rotY = make_rotY(30)
# print("rotY matrix")
# print_matrix(rotY)
# rotZ = make_rotZ(-45)
# print("rotZ matrix")
# print_matrix(rotZ)

parse_file( 'script', edges, transform, screen, color )
