age=int(input())
credit=int(input())
income=int(input())
has_loan=input()
if age<21:
    print("Rejected.")
else:
    if age>=21 and age<=59 and credit>=600 and credit<=749 and income>50000 and has_loan=="false":
        print("Approved.")
    elif age>=21 and age<=59 and credit>=750 and income>25000:
        print("Approved.")
    elif age>=60:
        if credit>=750:
            print("Approved.")
        else:
            print("Rejected.")
    else:
        print("Rejected.")