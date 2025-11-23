# Write a program to convert user given rupees into dollar and euro, pound

rupees = input("Enter Rupees : ")
rupees = int(rupees)
dollar = rupees/88
euro = rupees/102
pound = rupees/116
print(f"Rupees = {rupees} Dollar = {dollar} Euro = {euro} Pound = {pound}")