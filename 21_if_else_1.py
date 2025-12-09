#  write a program to findout which product is cheaper to purchase from 2 product's price and weight given by user

product_price_1 = float(input("Enter 1st product price : "))
product_weight_1 = float(input("Enter 1st product weight : "))

product_price_2 = float(input("Enter 2nd product price : "))
product_weight_2 = float(input("Enter 2nd product weight : "))

price_per_grams_1 = product_price_1/product_weight_1
price_per_grams_2 = product_price_2/product_weight_2

if price_per_grams_1 < price_per_grams_2:
    print(f"1st product is cheaper than 2nd product it save {price_per_grams_2 - price_per_grams_1} Rs.")
else:
    print(f"2nd product is cheaper than 1st product it save {price_per_grams_1 - price_per_grams_2} Rs.")