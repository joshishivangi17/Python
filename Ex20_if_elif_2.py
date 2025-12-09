# write a program to accept 2 number from user. and accept choice for operations.
# operations will be addition, subtraction, multiplication, division
# do operation and display result as per user choice using switch statements.

num1 = int(input("Enter Num1 : "))
num2 = int(input("Enter Num2 : "))

add = num1 + num2 #Addition
sub = num1 - num2 #Subtraction
multi = num1 * num2 #Multiplication
div = num1 / num2 #Division

# if you have answer of arithmetic operation, you must enter arithmetic sign(+,-,*,/) 
result = str(input("Enter sign between (+,-,*,/) : "))
if result == '+':
    print("Addition is ",add)
elif result == '-':
    print("Subtraction is ",sub)
elif result == '*':
    print("Multiplication is ",multi)
elif result == '/':
    print("Division is ",div)
else:
    print("Invalid input!!Please enter sign between (+,-,*,/)")
