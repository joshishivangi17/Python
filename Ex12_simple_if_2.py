#write a program to findout whether given shape is square or potrait or landscape using given length and width. (use simple if )

length = int(input("Enter Length value : "))
width = int(input("Enter Width value : "))

if length == width:
    print("It is Square")
if length > width:
    print("It is Landscape")
if length < width:
    print("It is Portrait")