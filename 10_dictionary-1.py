#Example of Dictionary

student = {'name' : 'Shivangi','weight' : 45.95,'age' : 21,'gender' : True,'mobile' : 1234567890}
print(student)
print(student['weight'])
print(student['age'])

#add new key value
student['city'] = 'Bhavnagar'
student['pincode'] = 364001
print(student)

#update 
student['name'] = 'Shraddha'
print(student)

#remove any one key value
del student['weight']
print(student)