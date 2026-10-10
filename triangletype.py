a=int(input("Enter a first side:"))
b=int(input("Enter a second side:"))
c=int(input("Enter a third side:"))
if a==b==c:
    print("It is Equilateral Triangle.")
elif a==b or b==c or a==c:
    print("It is Isosceles Triangle.")
else:
    print("It is Scalene Triangle.")