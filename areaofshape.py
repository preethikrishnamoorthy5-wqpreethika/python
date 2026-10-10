
shape = input()

if shape == "circle":
    r = float(input())
    area = 3.14 * r * r
    print("Area:", area)

elif shape == "rectangle":
    length = float(input())
    width = float(input())
    area = length * width
    print("Area:", area)

elif shape == "triangle":
    base = float(input())
    height = float(input())
    area = 0.5 * base * height
    print("Area:", area)

elif shape == "square":
    side = float(input())
    area = side * side
    print("Area:", area)

elif shape == "trapezoid":
    a = float(input())
    b = float(input())
    height = float(input())
    area = 0.5 * (a + b) * height
    print("Area:", area)

else:
    print("Invalid Shape")