#  write a program to findout only compound interest of given amount, rate, year 
# A = Final amount (after interest),P = Principal amount, R = Annual interest rate
# N = Number of times interest is compounded per year, T = Time in years 

p = int(input("Enter Principal Amount : "))
r = int(input("Enter Rate of interest : "))
t = int(input("Enter Time in years : "))

a = p * (1 + r / 100) ** t
compound_interest = a - p
print(f"Compound interest = {compound_interest}")