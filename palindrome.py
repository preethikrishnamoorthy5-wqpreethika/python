n=int(input())
ori=n
rev=0
while n>0:
    digit=n%10
    rev=digit+(rev*10)
    n=n//10
if rev==ori:
    print("Palindrome")
else:
    print("Not Palindrome")