a=int(input("Enter the number:"))
if a>=10 and a<=99:
    print("It is two-digit.")
elif a>=100 and a<=999:
    print("It is three-digit.")
elif a>=1000 and a<=9999:
    print("It is a four-digit.")
else:
    print("Not a digit.")