a=input()
sum=0
for i in a:
    n=int(i)
    if n%2==0:
        n+=1
    else:
        n-=1
    sum+=n
print(sum)