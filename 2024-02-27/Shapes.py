PI = 3.14

def circleArea(circleRadius):
    circleArea = PI * circleRadius * circleRadius
    return circleArea

def circlePer(circleRadius):
    circlePer = 2 * PI * circleRadius
    return circlePer

def rectArea(rectLen, rectBre):
    rectArea = rectLen * rectBre
    return rectArea

def rectPer(rectLen, rectBre):
    rectPer = rectLen * 2 + rectBre * 2
    return rectPer

def parrArea(parrLen, parrBre):
    parrArea = parrLen * parrBre
    return parrArea

def parrPer(parrLen, parrBre):
    parrPer = parrLen * 2 + parrBre * 2
    return parrPer

def triArea(triLen, triBre):
    triArea = 0.5 * triLen * triBre
    return triArea

def triPer(triBre):
    triPer = triBre * 3
    return triPer

def sphereVol(sphereRad):
    sphereVol = 4/3 * PI * (sphereRad ^ 3)
    return sphereVol

shape = input("Please input the shape to use: ")
val1 = int(input("Please input the first value: "))
val2 = int(input("Please input the second value, otherwise enter 0: "))

area = 0
per = 0

match shape:
    case "circle":
        area = circleArea(val1)
        per = circlePer(val1)
    case "rectangle":
        area = rectArea(val1, val2)
        per = rectPer(val1, val2)
    case "parallolagram":
        area = parrArea(val1, val2)
        per = parrPer(val1, val2)
    case "triangle":
        area = triArea(val1, val2)
        per = triPer(val1)
    case "sphere":
        area = sphereVol(val1)
    case _:
        print("Error, shape not found")

if shape == "sphere":
    print(f"You shape sphere has volume {area}")
else:
    print(f"Your shape {shape} has area {area} and perimeter {per}")