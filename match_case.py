
day: int = int(input("Enter a day and get it in a string (1-7):"))

if day == 1:
    print("Sunday");
elif day == 2:
    print("Monday");
elif day == 3:
    print("Tuesday");
elif day == 4:
    print("Wednesday");
elif day == 5:
    print("Thursday");
elif day == 6:
    print("Friday");
elif day == 7:
    print("Saturday");
else:
    print("Invalid day.");

match day:
    case 1:
        print("Sunday");
    case 2:
        print("Monday");
    case 3:
        print("Tuesday");
    case 4:
        print("Wednesday");
    case 5:
        print("Thursday");
    case 6:
        print("Friday");
    case 7:
        print("Saturday");
    case _:
        #else
        print("Invalid day.");

# match True:
#     case _ if age > 18 or balance < 100_00:
#           print('over 18')
#     case _ if age > 9:
#           print('over 9')
#     case _ if age > 2:
#           print('over 2')

