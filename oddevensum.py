n=input()
n=str(n)
evensum=0
oddsum=0
for i in n:
    digits=int(i)
    if digits%2==0:
        evensum+=digits
    else:
        oddsum+=digits
print(f"Sum of even digits:{evensum}")
print(f"Sum of odd digits:{oddsum}")