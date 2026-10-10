n=int(input())
product=1
while n>0:
    digits=n%10
    product*=digits
    n=n//10
print(product)