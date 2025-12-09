#write a program to accept product purchrase & sales price and findout profit or loss or break even amount (use if elif decision)

purchase_price = int(input("Enter purchase price : "))
sales_price = int(input("Enter sales price : "))

difference = sales_price - purchase_price
if difference > 0:
    print(f"You have earned profit of {difference} amount")
elif difference < 0:
    print(f"You have made loss of {difference} amount")
elif difference == 0:
    print(f"You have made no loss and earned no profit, break even")