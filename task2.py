#calculate the area of foundation of building
#ask user to enter the shape of the building ( square, rectangular or round)
#prompt for the appropriate dimensions, corresponding to shape
#calculate and display foundation area 
#a. square = length**2                                                 (looked up how to write a squared number maybe was covered in lectures but I'm behind I googled it)
#a. rectangle = length x width 
#a. circle = pi x radius**2 (πradius**2)

π = 3.1415    #defining variables at the beginning to be used later

shape = input("Please enter the shape of the building, you have the choice of square, rectangular or round: ")
if shape == "square":
    length = int(input("Please enter the length of the square: "))
    sqr_area = length**2
    print(f"The area of the building's foundation is: {sqr_area}")
elif shape == "rectangle":
    length = int(input("Please enter the length of the rectangle: "))
    width = int(input("Please enter the width of the rectangle: "))
    rect_area = length*width 
    print(f"The area of the building's foundation is: {rect_area}")
else:
    shape == "round"
    radius =  int(input("Please enter the radius of the circle: "))
    circle_area = π*radius**2
    print(f"The area of the building's foundation ≈ {circle_area}")     #I put the approximate, wavvy equals as I defined pi as an exact number
