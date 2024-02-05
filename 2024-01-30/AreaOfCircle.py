Radius = float(input("Input circle radius: ")) #Radius of the circle we want to calculate
PI = 3.14159 #Constant which gives us the value of PI for calculations

if Radius <= 0:
    print("Radius cannot be zero or smaller!")
else:
    Area = PI * Radius * Radius
    print("Area of circle with radius {0} is {1}".format(Radius, Area)) 