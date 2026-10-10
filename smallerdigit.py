n=input()
small=int(n[0])
for i in n:
    digits=int(i)
    if digits<small:
        small=digits
print(small)
