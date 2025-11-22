# Example of set

#Create dictionary
fruits = {'apple','grapes','banana','watermelon','orange','mango','guava','kiwi','chikkoo','cherry'}
print(fruits)

print("-----Add - pineapple-----")
fruits.add('pineapple')
print(fruits)

print("-----Remove - kiwi-----")
fruits.remove('kiwi')
print(fruits)

#Create list
list1 = ['strawberry','orange','papaya','pineapple','orange','apple','grapes','banana','watermelon','mango','orange','kiwi','cherry']
print(list1)

#Remove duplicate value from the list1 
list2 = set(list1)
print(list2)

num1 = {1,2,3,4}
num2 = {2,3,4,5}
print(f"Num1 : {num1}")
print(f"Num2 : {num2}")

#Display all value in one list (union)
union = num1.union(num2)
print("union",union)

#Display common value from both num1 - num2 (intersection)
intersection = num1.intersection(num2)
print("intersection",intersection)

#Display difference between both num1 - num2 (Difference)
difference = num1.difference(num2)  #different value of num1
print("difference of num1",difference)
difference = num2.difference(num1)  #different value of num2
print("difference of num2",difference)

