age=int(input())
night=int(input())
member=input()
total=0
if age<18:
    print("Booking Rejected")
else:
    if night==0:
        print("Invalid Nights")
    else:
        if night<=3:
            total=night*2000
        elif night<=7:
            total=night*1500
        else:
            total=night*1200
        dis=0
        disco=0
        if total>=10000:
            dis=total*0.05
        if member=="Yes":
            disco=total*0.10
        discount=dis+disco
        final=total-discount
        print(f"Room Charge:{total:.2f}")
        print(f"discount:{discount:.2f}")
        print(f"Final Bill:{final:.2f}")