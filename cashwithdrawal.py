a=input()
try:
    a=int(a)
    if a<=0:
        print("Enter a positive value.")
    elif a>50000:
        print("Withdrawal limit exceeded.")
    elif a%100!=0:
        print("Enter the amount multiple of 100.")
    else:
        print("Withdrawal successful.")
except ValueError:
    print("Invalid Format.")