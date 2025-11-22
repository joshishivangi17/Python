fruits = ('Mango','Banana','Apple')
box = (100,'Apple',3.14,True,None,False,'Apple')

print(fruits)
print(box)
print(fruits[0])
print(fruits[1:3])
print(fruits[1:])

print(fruits + box)
print("Position of Apple : ",fruits.index('Apple')) # get detail of Apple in fruits tuple using(fruits.index)
print("Count Apples in tuple : ",box.count('Apple')) # get detail of Apple in box tuple using(box.count)