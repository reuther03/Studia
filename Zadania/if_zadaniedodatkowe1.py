user_input = input("Enter a letter: ")

if user_input.isupper():
    print("Upper case")
elif user_input.islower():
    print("Lower case")
else:
    print("Not a letter")
