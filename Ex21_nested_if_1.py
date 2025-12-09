# write a program to accept month number from user and display how many days month has. 
#     input : 1 output : this month has 31 days 
#     input : 4 output : this month has 30 days 
# 1,3,5,7,8,10,12 - 31 days in this month
# 4,6,9,11 - 30 days in this month
# 2 - 28/29 days in this month

month = int(input("Enter number between (1 to 12) : "))

if month <= 12:
    if (month == 4) or (month == 6) or (month == 9) or (month == 11):
        print(f"{month} this month has 30 days.")
    elif (month == 2):
        print(f"{month} this month has 28/29 days.")
    else:
        print(f"{month} this month has 31 days.")
else:
    print("Invalid input!!Please enter number between (1 to 12)")

