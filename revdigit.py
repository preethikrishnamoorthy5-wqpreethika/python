n=int(input())
n=str(n)
sum=0
rev=0
for i in n:
    digits=int(n)
    rev=digits%10
    sum=rev+(sum*10)
    digits/=10
print(sum)

        