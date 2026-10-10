a=int(input("Enter the x-axis:"))
b=int(input("Enter the y-axis:"))
if a>0  and b>0:
    print("Quadrant I")
elif a<0 and b>0:
    print("Quadrant II")
elif a<0 and b<0:
    print("Quadrant III")
else:
    print("Quadrant IV")