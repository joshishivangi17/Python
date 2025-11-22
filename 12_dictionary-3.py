# Example Of Dictionary

subject = {'course' : 'cyber security','trainer' : 'harshil jasoliya','duration' : 240}
print(subject)
subject2 = subject.copy()
print(subject2)

# Update
subject2.update({'course' : 'AI/ML/DS'})
subject2.update({'fees' : 40000})
print(subject2)
print(subject2['fees'])

#Get value
print(subject2.get('city')) #None
print(subject2.get('city','Not Found')) #Not Found
print(subject2)

#Get keys of dictionary
print(subject2.keys())

#Get value of dictionary
print(subject2.values())

#Get item of dictionary
print(subject2.items())

#Remove specific value & key from dictionary
subject2.pop('duration')
print(subject2)

#Remove last key or last value from dictionary
subject2.popitem()
print(subject2)

#Create dictionary using list
student = ['name','mobile','email']
shivangi = dict.fromkeys(student)
print(shivangi)
shivangi.update({'name' : 'shivangi joshi'})
shivangi.update({'mobile' : 1234567890})
shivangi.update({'email' : 'shivangi@gmail.com'})
print(shivangi)