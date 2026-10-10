a=int(input("Enter a number:"))
if a>0 and a<=100:
    bill=a*2
    print("Bill= ",bill)
elif a>100 and a<=200:
    bill=200+((a-100)*3)
    print("Bill= ",bill)
else:
    bill=500+((a-200)*5)
    print("Bill= ",bill)