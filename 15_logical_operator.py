#Example of logical operators in python
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))

#Logical AND Operator (return value true if both the statements are true, otherwise false)
AND_operation = (num1 == num2) and (num2 == num3)
print(f"AND : {AND_operation}")

#Logical OR Operator (return value true if at least one statement is true)
OR_operation = (num1 == num2) or (num2 == num3)
print(f"OR : {OR_operation}")

#Logical NOT Operator (if the statement is true, it returns false and vice versa)
NOT_operation = not(num1 == num2)
print(f"NOT : {NOT_operation}")
