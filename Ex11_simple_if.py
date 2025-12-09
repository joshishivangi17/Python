# write a program to convert 24 hours time into 12 hours format time and display it with AM PM message. (using simple if )
# input : 15 hours 
# output  3 PM 

# input : 11 hours 
# output  11 AM 

# input : 25 hours 
# output  invalid input 

hours = int(input("Enter Hours (1-24) : "))

if hours < 0 and hours > 24:
    print(hours,"Invalid Time")
if hours > 0 and hours < 12:
    print(hours,"A.M.")
if hours == 12:
    print("12 A.M.")
if hours > 12 and hours < 24:
    print(hours - 12,"P.M.") 
if hours == 24:
    print("12 P.M.")


