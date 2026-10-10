try:
     num = int(input("Enter a number: "))
     print(100 / num)
except ValueError:
     print("Please enter a valid integer.")
except ZeroDivisionError:
     print("Cannot divide by zero.")
else:
     print("Operation completed successfully.")
finally:
     print("Program finished.")