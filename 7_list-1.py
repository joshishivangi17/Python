#Create list
fruits = ['apple','mango','pineapple','kiwi','cherry']
box = [100,'apple',3.14,True,False,None]

print(fruits)
print(box)
print(fruits[0])
print(box[2])
print(fruits[1:])
print(box[2:])
print(fruits[1:4])
print(box[1:5])

print(fruits * 2)
print(fruits + box)

#We can change list as list is mutable
fruits[3] = 'strawberry'
print(fruits)
del fruits[1]
print(fruits)
fruits.append('watermelon')
print(fruits)


