# write a program to accept birth day and birth month from user. decide zodiac sign from below table 
#     Aries: March 21–April 19
#     Taurus: April 20–May 20
#     Gemini: May 21–June 21
#     Cancer: June 22–July 22
#     Leo: July 23–August 22
#     Virgo: August 23–September 22
#     Libra: September 23–October 22
#     Scorpio: October 24–November 21
#     Sagittarius: November 22–December 21
#     Capricorn: December 22–January 19
#     Aquarius: January 20–February 18
#     Pisces: February 19–March 20

day = int(input("Enter Birth day (1 to 31) : "))
month = str(input("Enter Birth month (january to december): "))

if day <= 31:
    if (day >=21) and (month == 'march') or (day <=19) and (month == 'april'):
        print("Zodiac sign : Aries")
    elif (day >=20) and (month == 'april') or (day <=20) and (month == 'may'):
        print("Zodiac sign : Taurus")
    elif (day >=21) and (month == 'may') or (day <=21) and (month == 'june'):
        print("Zodiac sign : Gemini")
    elif (day >=22) and (month == 'june') or (day <=22) and (month == 'july'):
        print("Zodiac sign : Cancer")
    elif (day >=23) and (month == 'july') or (day <=22) and (month == 'august'):
        print("Zodiac sign : Leo")
    elif (day >=23) and (month == 'august') or (day <=22) and (month == 'september'):
        print("Zodiac sign : Virgo")
    elif (day >=23) and (month == 'september') or (day <=22) and (month == 'october'):
        print("Zodiac sign : Libra")
    elif (day >=24) and (month == 'october') or (day <=21) and (month == 'november'):
        print("Zodiac sign : Scorpio")
    elif (day >=22) and (month == 'november') or (day <=21) and (month == 'december'):
        print("Zodiac sign : Sagittarius")
    elif (day >=22) and (month == 'december') or (day <=19) and (month == 'january'):
        print("Zodiac sign : Capricorn")
    elif (day >=20) and (month == 'january') or (day <=18) and (month == 'february'):
        print("Zodiac sign : Aquarius")
    elif (day >=19) and (month == 'february') or (day <=20) and (month == 'march'):
       print("Zodiac sign : Pisces")       
else:
    print("Please enter valid input!!")
