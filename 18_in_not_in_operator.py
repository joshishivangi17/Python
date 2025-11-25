#Example of in not in operator in python

countries = ["Japan","Brazil","Germany","India","Australia","Canada","South Korea","Argentina","Sweden","Thailand","Mexico","Italy","Nigeria","Spain","Egypt","New Zealand","South Africa","Norway","Indonesia","France"]
print(countries)

my_country = input("Where are you from (country)? : ")
result = my_country in countries
print(f"result = {result}")

g20 = ["Argentina", "Australia", "Brazil", "Canada", "China","France", "Germany", "India", "Indonesia", "Italy","Japan", "Mexico", "Russia", "Saudi Arabia", "South Africa", "South Korea", "Turkey","European Union", "African Union"]
print(g20)

g20_country = input("Give one country name which is not a member of g20 : ")
result2 = g20_country not in g20
print(f"result2 = {result2}")
