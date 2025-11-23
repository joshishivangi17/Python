#  create a python program to create 2 set. 
#     1 set has list of sports include in olympic 2016
#     2 set has list of sports include in olympic 2022

#     display both set 
#     findout unique sports in both set & display it 
#     findout common sports in both set & display it 
#     findout sports in olympic 2022 but not in 2016 & display it 

olympic1 = {'Badminton','Basketball','Football','Boxing'}
olympic2 = {'Boxing','Cycling','Golf','Judo'}

print(f"Olympic 2016 : {olympic1}")
print(f"Olympic 2022 : {olympic2}")

#Display both set (union)
union = olympic1.union(olympic2)
print("Union",union)

#Unique sports of both set (difference)
difference = olympic1.difference(olympic2) #Unique value of olympic1
print("Difference of Olympic 2016",difference)

difference = olympic2.difference(olympic1) #Unique value of olympic2
print("Difference of Olympic 2022",difference)

#Common sports of both set (intersection)
intersection = olympic1.intersection(olympic2)
print("Common sports of both Olympic",intersection)

#Display only those sports which in olympic 2022 but not in 2016 (difference)
difference = olympic2.difference(olympic1) #Unique value of olympic2
print("Differece of Olympic 2022",difference)




