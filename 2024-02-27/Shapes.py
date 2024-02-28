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
    case "circle": print("Your shape circle has area", circleArea(val1), "and perimeter", circlePer(val1))
    case "rectangle": print("Your shape rectangle has area", rectArea(val1, val2), "and perimeter", rectPer(val1, val2))
    case "parallolagram": print("Your shape parallolagram has area", parrArea(val1, val2), "and perimeter", parrPer(val1, val2))
    case "triangle": print("Your shape triangle has area", triArea(val1, val2), "and perimeter", triPer(val1))
    case "sphere": print("Your shape sphere has volume", sphereVol(val1))
    case _: print("Error, shape not found")