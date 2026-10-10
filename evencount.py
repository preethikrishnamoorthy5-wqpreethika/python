n=input()
n=str(n)
count=0
for i in n:
    digits=int(i)
    if digits%2==0:
        count+=1
print(count)