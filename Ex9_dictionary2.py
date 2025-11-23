# Create Dictionary to store your college details like name, trust, pricipal, establishment year, address, city, courses etc 
#     print dictionary 
#     update city using update method 
#     add state using update methods 
#     display all keys using keys method 
#     display all values using values method 
#     remove state using pop method 
#     remove last item using pop item method 
#     remove all key value pair 
#     copy dictionary using copy method 

college = {"name" : "SSCCS","trust" : "KP Swami","principle" : "Paresh Rathod", "Established year" : 1987,"address" : "Sardarnagar","city" : "Bhavnagar","courses" : "BCA/BBA/Bcom"}
print(college)

#Update city using update method
college.update({'city' : 'Ahmedabad'})
print(college)

#Add state using update method
college.update({'state' : 'Gujarat'})
print(college)

#Display all keys using Keys method
print(college.keys())

#Display all values using values method
print(college.values())

#Remove state using pop method
college.pop('state')
print(college)

#Remove last item using pop item method
college.popitem()
print(college)

#Copy Dictionary using copy method
college1 = college.copy()
print("college1",college1)

#Remove all key value pair
college.clear()
print(college)
