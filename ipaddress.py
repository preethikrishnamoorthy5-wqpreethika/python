a=input()
b=input()
cout1=a.count('.')
cout2=b.count('.')
c=a.split('.')
d=b.split('.')
if cout1==2 and cout2==2:
    if a==b:
        print("Same")
    else:
        print("Different")
        if c[2]>d[2]:
            print(a,"is greater")
        elif c[2]<d[2]:
            print(b,"is greater")
        elif c[1]>d[1]:
            print(a,"is greater")
        elif c[1]<d[1]:
            print(b,"is greater")     
        elif c[0]>d[0]:
            print(a,"is greater")
        else:
            print(b,"is greater")
else:
    print("Invalid format!! Enter valid format.....")