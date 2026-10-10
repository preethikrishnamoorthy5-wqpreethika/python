n=int(input())
n=str(n)
a=int(input())
count=0
for i in n:
    digits=int(i)
    if(digits==a):
        count+=1
print(count)