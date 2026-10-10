a=input()
b=input()
cout1=a.count('/')
cout2=b.count('/')
if cout1==cout2:
    if a==b:
        print("Both the dates given are same.")
    else:
        print("Different.")
        x=a.split('/')
        y=b.split('/')
        if x[2]>y[2]:
            print(a)
        elif x[2]<y[2]:
            print(b)
        elif x[1]>y[1]:
            print(a)
        elif x[1]<y[1]:
            print(b)
        elif x[0]>y[0]:
            print(a)
        else:
            print(b)
else:
    print("Invalid Format please enter the valid Format!!")