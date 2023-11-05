from Triangles import *
from Quadrilaterals import *
from Functions import *

while True:
    welcome_menu()
    menu_selection = int(input("\nPlease choose a shape: "))

    if menu_selection == 1:

        polygon_menu()

        shape_selection = int(input("\nPlease choose a polygon: "))
        if shape_selection == 1:
            number_of_sides = int(input("Please enter the number of sides: "))
            side_len = float(input("Please enter the side length: "))

            polygon_1 = Polygon(number_of_sides, side_len)
            actions_menu()

            action_selection = int(input("\nPlease choose an action: "))
            if action_selection == 1:
                perimeter = polygon_1.perimeter()
                print(perimeter)
            elif action_selection == 2:
                area = polygon_1.area()
                print(area)
            elif action_selection == 3:
                polygon_1.draw()

        elif shape_selection == 2:
            side_len = float(input("Please enter the side length: "))

            pentagon_1 = Pentagon(side_len)
            actions_menu()

            action_selection = int(input("\nPlease choose an action: "))
            if action_selection == 1:
                perimeter = pentagon_1.perimeter()
                print(perimeter)
            elif action_selection == 2:
                area = pentagon_1.area()
                print(area)
            elif action_selection == 3:
                pentagon_1.draw()

        elif shape_selection == 3:
            side_len = float(input("Please enter the side length: "))

            hexagon_1 = Hexagon(side_len)
            actions_menu()

            action_selection = int(input("\nPlease choose an action: "))
            if action_selection == 1:
                perimeter = hexagon_1.perimeter()
                print(perimeter)
            elif action_selection == 2:
                area = hexagon_1.area()
                print(area)
            elif action_selection == 3:
                hexagon_1.draw()

        elif shape_selection == 4:
            side_len = float(input("Please enter the side length: "))

            octagon_1 = Octagon(side_len)
            actions_menu()

            action_selection = int(input("\nPlease choose an action: "))
            if action_selection == 1:
                perimeter = octagon_1.perimeter()
                print(perimeter)
            elif action_selection == 2:
                area = octagon_1.area()
                print(area)
            elif action_selection == 3:
                octagon_1.draw()

    elif menu_selection == 2:
        triangle_menu()

        shape_selection = int(input("\nPlease choose a triangle: "))
        if shape_selection == 1:
            side_len_1 = float(input("Please enter the first side length: "))
            side_len_2 = float(input("Please enter the second side length: "))
            side_len_3 = float(input("Please enter the third side length: "))
            base = float(input("Please enter the base length: "))
            height = float(input("Please enter the height length: "))
            angle_1 = float(input("Please enter the first angle (between 1st & 2nd sides): "))
            angle_2 = float(input("Please enter the first angle (between 2nd & 3rd sides): "))

            triangle_1 = Triangle(side_len_1, side_len_2, side_len_3, base, height, angle_1, angle_2)
            actions_menu()

            action_selection = int(input("\nPlease choose an action: "))
            if action_selection == 1:
                perimeter = triangle_1.perimeter()
                print(perimeter)
            elif action_selection == 2:
                area = triangle_1.area()
                print(area)
            elif action_selection == 3:
                triangle_1.draw()

        elif shape_selection == 2:
            side_len_1_rep = float(input("Please enter the first & second side length: "))
            side_len_2 = float(input("Please enter the third side length: "))
            base = float(input("Please enter the base length: "))
            height = float(input("Please enter the height length: "))
            angle_1 = float(input("Please enter the opposite angle (1st between non-equal sides sides): "))

            iso_triangle_1 = IsoTriangle(side_len_1_rep, side_len_2, base, height, angle_1)
            actions_menu()

            action_selection = int(input("\nPlease choose an action: "))
            if action_selection == 1:
                perimeter = iso_triangle_1.perimeter()
                print(perimeter)
            elif action_selection == 2:
                area = iso_triangle_1.area()
                print(area)
            elif action_selection == 3:
                iso_triangle_1.draw()

        elif shape_selection == 3:
            side_len = float(input("Please enter the side length: "))

            equi_triangle_1 = EquiTriangle(side_len)
            actions_menu()

            action_selection = int(input("\nPlease choose an action: "))
            if action_selection == 1:
                perimeter = equi_triangle_1.perimeter()
                print(perimeter)
            elif action_selection == 2:
                area = equi_triangle_1.area()
                print(area)
            elif action_selection == 3:
                equi_triangle_1.draw()

    elif menu_selection == 3:
        quadrilateral_menu()

        shape_selection = int(input("\nPlease choose a quadrilateral: "))
        if shape_selection == 1:
            side_len_1 = float(input("Please enter the first side length: "))
            side_len_2 = float(input("Please enter the second side length: "))
            side_len_3 = float(input("Please enter the third side length: "))
            side_len_4 = float(input("Please enter the fourth side length: "))
            angle_1 = float(input("Please enter the first angle (between 1st & 2nd sides): "))
            angle_2 = float(input("Please enter the second angle (between 2nd & 3rd sides): "))
            angle_3 = float(input("Please enter the third angle (between 3rd & 4th sides): "))

            quad_1 = Quadrilateral(side_len_1, side_len_2, side_len_3, side_len_4, angle_1, angle_2, angle_3)
            actions_menu()

            action_selection = int(input("\nPlease choose an action: "))
            if action_selection == 1:
                perimeter = quad_1.perimeter()
                print(perimeter)
            elif action_selection == 2:
                area = quad_1.area()
                print(area)
            elif action_selection == 3:
                quad_1.draw()

            elif shape_selection == 2:
                side_len = float(input("Please enter the side length: "))
                square_1 = Square(side_len)
                actions_menu()
                action_selection = int(input("\nPlease choose an action: "))
                if action_selection == 1:
                    perimeter = square_1.perimeter()
                    print(perimeter)
                elif action_selection == 2:
                    area = square_1.area()
                    print(area)
                elif action_selection == 3:
                    square_1.draw()

            elif shape_selection == 3:
                side_len_1 = float(input("Please enter the first side length: "))
                side_len_2 = float(input("Please enter the second side length: "))

                rect_1 = Rectangle(side_len_1, side_len_2)
                actions_menu()

                action_selection = int(input("\nPlease choose an action: "))
                if rect_1 == 1:
                    perimeter = rect_1.perimeter()
                    print(perimeter)
                elif action_selection == 2:
                    area = rect_1.area()
                    print(area)
                elif action_selection == 3:
                    rect_1.draw()

    elif menu_selection == 4:
        break

    else:
        print("Please choose a valid option!")
