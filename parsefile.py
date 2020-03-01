from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    if (f.mode == "r"):
        line = f.readline()
        while(line):
            # print('"' + line.strip() + '"')
            if (line == "line\n"):
                args = f.readline()
                # print(args)
                coordinates = args.split(" ")
                # print(coordinates)
                coordinates[5] = coordinates[5].strip()
                for x in range (len(coordinates)):
                    coordinates[x] = int(coordinates[x].strip())
                add_edge(points, coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5])
                # print_matrix(points)
            elif (line == "ident\n"):
                ident(transform)
                # print_matrix(transform)
            elif (line == "scale\n"):
                args = f.readline()
                scalars = args.split(" ")
                scalars[2] = str(scalars[2].strip())
                for x in range (len(scalars)):
                    scalars[x] = int(scalars[x])
                # print(scalars)
                scale_matrix = make_scale(scalars[0], scalars[1], scalars[2])
                # print_matrix(scale_matrix)
                matrix_mult(scale_matrix, transform)
                # print_matrix(transform)
            elif (line == "move\n"):
                args = f.readline()
                units = args.split(" ")
                units[2] = str(units[2].strip())
                for x in range (len(units)):
                    units[x] = int(units[x])
                # print(units)
                translate_matrix = make_translate(units[0], units[1], units[2])
                # print_matrix(translate_matrix)
                matrix_mult(translate_matrix, transform)
                # print_matrix(transform)
            elif (line == "rotate\n"):
                args = f.readline()
                split_args = args.split(" ")
                theta = int(split_args[1].strip())
                # print(split_args)
                if (split_args[0] == "x"):
                    rotate_matrix = make_rotX(theta)
                elif (split_args[0] == "y"):
                    rotate_matrix = make_rotY(theta)
                elif (split_args[0] == "z"):
                    rotate_matrix = make_rotZ(theta)
                # print_matrix(rotate_matrix)
                matrix_mult(rotate_matrix, transform)
                # print_matrix(transform)
            elif (line == "apply\n"):
                matrix_mult(transform, points)

            elif (line == "display\n"):
                # print_matrix(points)
                clear_screen(screen)
                draw_lines(points, screen, color)
                # display(screen)

            elif (line == "save\n"):
                clear_screen(screen)
                draw_lines(points, screen, color)
                save_ppm(screen, "image.ppm")
                save_extension(screen, line)

            elif (line == "quit\n"):
                line = None
            line = f.readline()
    f.close()
