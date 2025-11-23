#List related methods
fruits = []
fruits.append('orange')
fruits.append('mango')
fruits.append('kiwi')
fruits.append('strawberry')
fruits.append('apple')
print(fruits)

#Insert intem in begining
fruits.insert(0,'pineapple')
fruits.insert(1,'watermelon')
print(fruits)

#Remove by value
fruits.remove('kiwi')
print(fruits)

#Remove by position
fruits.pop(1)
print(fruits)

#Add item in last 
fruits.append('cherry')
print(fruits)

#Findout position of value
position = fruits.index('orange')
print(position)

#Count value of item
coconut_count = fruits.count('coconut')
print(coconut_count)

#Extend value (combine value)
vegis = ['potato','tomato','chilly']
print(vegis)
fruits.extend(vegis)
print(fruits)

#Clear value of vegis
vegis.clear()
print(vegis)

#Sort value of fruits
fruits.sort()
print(fruits)

#Reverse value of fruits
fruits.reverse()
print(fruits)

#Copy list in another list
fruits1 = fruits.copy()
print(fruits1)

#Clear value of copy list
fruits1.clear()
print(fruits,fruits1)
