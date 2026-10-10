a=input("Enter the alpha:")
if a.isalpha():
    if a in "aeiouAEIOU":
        print("Vowel.")
    else:
        print("Consonant.")
else:
    print("Invalid input.")
    