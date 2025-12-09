# write a program to accept day of week (between 1 to 7) and then display name of day. (use simple if decision making)
#     input 1 : monday 
#     input 2 : tuesday 
#     input 7 : sunday 

days = int(input("Enter number of day (1-7) : "))

if days < 1 or days > 7:
    print("Invalid value! Please enter number between 1 to 7")
if days == 1:
    print("Monday")
if days == 2:
    print("Tuesday")
if days == 3:
    print("Wednesday")
if days == 4:
    print("Thursday")
if days == 5:
    print("Friday")
if days == 6:
    print("Saturday")
if days == 7:
    print("Sunday")

