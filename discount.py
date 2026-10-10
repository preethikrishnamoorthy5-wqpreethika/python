a=input()
discount=0
final=0
try:
    a=int(a)
    if a<0:
        print("Invalid amount.")
    elif a==0:
        print("No purchase.")
    elif a>=1 and a<=999:
        discount=0
        final=a
        print(f"Original Amount :{a:.2f}")
        print(f"Discount :{discount:.2f}")
        print(f"Final Amount :{final:.2f}")
    elif a>=1000 and a<=4999:
        discount=a-(a*0.10)
        final=a+discount
        print(f"Original Amount :{a:.2f}")
        print(f"Discount :{discount:.2f}")
        print(f"Final Amount :{final:.2f}")
    else:
        discount=a-(a*0.20)
        final=a+discount
        print(f"Original Amount :{a:.2f}")
        print(f"Discount :{discount:.2f}")
        print(f"Final Amount :{final:.2f}")
except ValueError:
    print("Invalid Format.")