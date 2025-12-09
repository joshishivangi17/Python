#  write a program to findout whether given year is millenium year or not 
# Millenium year - 1,1001,2001...

year = int(input("Enter year : "))

if year % 1000 == 1:
    if year > 0 :
        print("This year is millenium year")
    else:
        print(f"This year {year} is divisible by 1000 but not a positive year")
else:
    print("This year is not a millenium year")
