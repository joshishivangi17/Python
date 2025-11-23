# create dictionary of your college & store 
#         name, 
#         pricipal name 
#         establishment year 
#         area 
#         courses 
#     update courses name 
#     remove establishment year 
#     print dictionary 
#     add staff key which is list and has 5 teacher names 
#     add floor key which is tuples and has number of class room on particular floor 
#     print dictionary 
#     add one more staff shivangi 
#     remove staff named as khyati 
#     remove key value pair floor 
#     print dictionary 

college = {'name' : 'Shree Swaminarayan College Of Computer Science','principal name' : 'Pareshbhai Kukdiya','establishment year' : 1985,'area' : 'Sardarnagar, Bhavnagar-364001','courses' : 'BCA, BSC IT, BBA, B.Com'}
print(college)
college.pop('establishment year')
print(college)
college['staff'] = ['Khyati Baraiya','Shraddha Joshi','Vandit Belani','Harshil Jasoliya','Karishna Pandya']
college['floor'] = (1, 2, 3, 4, 5)
print(college)
college['staff'].append('Shivangi Joshi')
print(college)
college['staff'].remove('Khyati Baraiya')
print(college)
del college['floor']
print(college)

