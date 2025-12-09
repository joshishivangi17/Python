# write a program to findout which is cheaper approach to buy IPhone 17 pro max.  
# consider use is going usa should he buy iphone from usa or from india. 

price_of_india = int(input("Enter price of IPhone 17 pro max in India : "))
price_of_usa = int(input("Enter price of IPhone 17 pro max in USA : "))

if price_of_india < price_of_usa:
    print(f"Price_of_India {price_of_india} is cheaper than USA")
else:
    print(f"Price_of_USA {price_of_usa} is cheaper than India")


