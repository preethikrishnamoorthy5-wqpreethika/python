dis=int(input())
hour=int(input())
age=int(input())
if hour>=0 and hour<=23:
    if dis>0 and dis<=5:
        tot=100
    elif dis>5 and dis<=15:
        tot=100+(dis-5)*15
    else:
        tot=250+(dis-15)*10
    if hour>=22 or hour<=5:
          tot=tot+(tot*0.20)
    if age>=60:
          tot=tot-(tot*0.10)
    print(tot)
else:
    print("Invalid Hours.")