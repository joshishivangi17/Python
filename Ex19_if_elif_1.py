#  Write a program that takes a 5 subject marks from user. calculate total and Percentage  and prints the grade using the following conditions: also display total and Percentage

# | Percentage | Grade |
# | ---------- | ----- |
# | 90–100     | A+    |
# | 80–89      | A     |
# | 70–79      | B     |
# | 60–69      | C     |
# | 50–59      | D     |
# | below 50   | Need to improve  |
# ----------------------------------------

marks = [0,0,0,0,0]

marks[0] = int(input("Enter sub1 mark : "))
marks[1] = int(input("Enter sub2 mark : "))
marks[2] = int(input("Enter sub3 mark : "))
marks[3] = int(input("Enter sub4 mark : "))
marks[4] = int(input("Enter sub5 mark : "))

print(f"5 Subject marks : {marks}")
total = marks[0] + marks[1] + marks[2] + marks[3] + marks[4]
percentage = total/5

if percentage >= 90: 
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Need to Improve"

print("Total : ",total)
print(f"Percentage : {percentage}%")
print("Grade : ",grade)
