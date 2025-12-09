# write a program to accept length and width of two different farm from user. and findout & display which farm is bigger 

#farm1
print("-----Farm1-----")
length = int(input("Enter Length : "))
width = int(input("Enter Width : "))

farm1 = length * width
print("Farm1 : ",farm1)

#farm2
print("-----Farm2-----")
length1 = int(input("Enter Length1 : "))
width1 = int(input("Enter Width1 : "))

farm2 = length1 * width1
print("Farm2 : ",farm2)

print("---Which farm is Bigger?---")
if farm1 > farm2:
    print("Farm 1 is Bigger")
if farm1 < farm2:
    print("Farm 2 is Bigger")


