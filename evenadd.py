n=int(input())
a=str(n)
sum=1
total=0
for i in a:
    digits=int(i)
    if digits%2==0:
        sum*=digits
print(sum)
