# write a program to findout whether given year is millennium year or not. using if else decision making statements.
#Millennium year ex.: 1,1001,2001,3001...

year = int(input("Enter Year : "))

if year % 1000 == 1:
    print(f"This {year} is Millennium year")
else:
    print(f"This {year} is not Millennium year")