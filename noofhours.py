hours=input()
attend=input()
if hours.isdigit() and attend.isdigit():
    hours=int(hours)
    attend=int(attend)
    if hours>0 and hours<=100 and attend>0 and attend<=100:
        att=attend/hours*100
        print(f"{att:.2f}")
        if att>=75:
            print("Permitted")
        else:
            print("Not Permitted")
    else:
        print("Enter the value between 1 to 100.")
else:
    print("Enter the valid format")