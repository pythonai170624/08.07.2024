
# read number from user,
# print positive, negative or zero

number: int = int(input("enter number:"));

if number > 0:
    print(f"{number} is Positive");
elif number < 0:
    print(f"{number} is Negative");
else:
    print(f"{number} is Zero");

if number == 0:
    print(f"{number} is Zero");
elif number > 0:
    print(f"{number} is Positive");
else:
    print(f"{number} is Negative");

print("Goodbye!")