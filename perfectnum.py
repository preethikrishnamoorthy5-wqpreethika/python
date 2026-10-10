n=int(input())
original=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==original:
    print("Perfect")
else:
    print("Not Perfect")
