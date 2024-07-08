
# we require age bigger than 18 and more than 100,000 balance
age: int = int(input("what's your age?"));
balance: int = int(input("what's your balance?"));

# easiest way
# short-circuit logic: if 1st is false do not check the 2nd
# if [internet-is-working] and [go-to-bank-isreal-check-ribit-prime > 6%]
if age > 18 and balance > 100_000:
    print("you are qualified for the program");
else:
    print("you are NOT qualified for the program");

# nested if.
# check age , only if bigger than 18 then check balance
if age > 18:
    ##
    ##
    ##
    if balance > 100_000:
        print("you are qualified for the program");
    else:
        print("you are NOT qualified for the program");
else:
    print("you are NOT qualified for the program");


# check the same but with not
if not age <= 18 and not balance <= 100_000:
    print("you are qualified for the program");
else:
    print("you are NOT qualified for the program");

# using or instead of and
if age <= 18 or balance <= 100_000:
    print("you are NOT qualified for the program");
else:
    print("you are qualified for the program");

# solving with elif
if age > 18 and balance <= 100_000:
    print("you are NOT qualified for the program due to your balance");
elif balance > 100_000 and age <= 18:
    print("you are NOT qualified for the program due to your age");
else:
    print("you are qualified for the program");

if age >= 18 or age < 18:
    print("always")
else:
    # will never reach here
    print("not always")
