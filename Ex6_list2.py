# do following operation on list
#     create list of friend 
#     add 2 friend name at begining 
#     add 2 friends name at last 
#     create another list of relative 
#     append relative list into friend 
#     remove 1st item in friend 
#     remove friend whose name is samir 
#     clear friend list 

friends = ['Shivangi','Shraddha','Krupa']
print(friends)
friends.insert(0,'Ankita')
friends.insert(1,'Shruti')
print(friends)
friends.append('Sneha')
friends.append('Shweta')
print(friends)
relative = ['Rina','Swati','Samir']
print(relative)
friends.extend(relative)
print(friends)
relative.pop(1)
print(relative)
relative.remove('Samir')
print(relative)
relative.clear()
print(friends)

