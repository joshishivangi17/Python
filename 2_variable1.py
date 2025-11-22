#How to create variable
#Syntex : variable_name = value

print("----Use of Variable----")
name = "Shivangi"
print(name)
age = 21
print(age)
pi = 3.14
print(pi)
gender = True
print(gender)

#Display multiple text using variable in single line

print("----Multiple text in single line----")
name = "Shraddha"
age = 19
pi = 3.14
gender = True
print(name,age,pi,gender)

#We can use variable inside String 

print("----Variable inside String----")
name = "Shivangi"
age = 21
pi = 3.14
print(f"My name is {name}.I am {age} year old.PI value is {pi}")

# We can delete variable also
#Syntex : del variable_name

del pi
# print(pi) [when del function is used then 
# this print function is not display the value of pi because pi variable is deleted by del function]
print("Good Bye")


