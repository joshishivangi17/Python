# create a list to store your friends name in list (minimum 5)
#     - display whole list 
#     - display 1st friend 
#     - display last friend
#     - replace 1st friend with some other value 
#     - remove last value from list 
#     - display 1st 3 value in list 
#     - display last 3 value in list 

friends = ['Shivangi','Shraddha','Krupa','Mansi','Sneha']
print(friends)
print(friends[0])
print(friends[4])
friends[0] = 'Mishita'
print(friends)
friends.remove('Sneha')
print(friends)
print(friends[0:3])
print(friends[1:4])
