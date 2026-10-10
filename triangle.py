a=int(input("Enter a first side:"))
b=int(input("Enter a second side:"))
c=int(input("Enter a third side:"))
if a+b>c and b+c>a and c+a>b:
    print("It is valid triangle.")
else:
    print("It is invalid triangle.")