a=input()
b=input()
bonus=0
try:
    a=int(a)
    if a <0:
        print("Invalid amount")
    elif a==0:
        print("No recharge")
    elif a>0 and a<=199:
        bonus=0
    elif a>199 and a<=499:
        bonus=a*0.05
    elif a>499 and a<=999:
        bonus=a*0.10
    else:
        bonus=a*0.15
    if b == "new":
        bonus = bonus + 50
    elif b == "regular":
        bonus = bonus
    else:
        print("Invalid Customer Type.")
        
        # Final value
    if b == "new" or b == "regular":
        final = a + bonus

        print(f"Recharge Amount : {a:.2f}")
        print(f"Bonus : {bonus:.2f}")
        print(f"Final Value : {final:.2f}")
except ValueError:
    print("Invalid Format.")