# 9 / 2 = 4.5
# 4 1/2
# 9/2 = 4 module 1
# 9       1 == module
# _  =  4 _
# 2       2

# 8/3 = 2 module 2 = 2 2/3
# 8       2 == module
# _  =  2 _
# 3       3

# 4 / 2 = 2 module 0
# 98 % 10 ==> 8
# 74 % 10 ==> 4
# 74        4 == module
# __  =  7 __
# 10       10

# 74 % 13 ==> 9
# 74        9 == module
# __  =  5 __
# 13       13

# 10 % 2 = module 0
# 11 % 2 = module 1
# 9 % 3 = module 0
# 9       0 == module
# _  =  3 _
# 3       3

# 10 % 3 = module 1
# 10      1 == module
# _  =  3 _
# 3       3

number: int = int(input("Give me a number?"));
# 9 / 2 = 4.5
# 8 / 2 = 4.0
print(f"{number} / 2 = {number / 2}")
print(f"{number} % 2 = {number % 2}")
if number % 2 == 0: # is the sheerit when divide by 2 is equal to 0
    print(f"{number} is Zugi even");
else:
    print(f"{number} is E-Zugi odd");
