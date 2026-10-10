n=input()
lar=int(n[0])
for i in n:
    digits=int(i)
    if digits>lar:
        lar=digits
print(lar)