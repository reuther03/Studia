a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. dodawanie")
print("2. odejmowanie")
print("3. mnozenie")
print("4. dzielenie")
print("5. potegowanie")
operation = input("podaj oprracje: ")




if operation == "1":
    result = a + b
elif operation == "2":
    result = a - b
elif operation == "3":
    result = a * b
elif operation == "4":
    if b == 0:
        result = "nie dziel przez zero"
    else:
        result = a / b
elif operation == "5":
    result = a ** b
else:
    result = "zle dzialanie"

print("wynik: ", result)
