# write a program to decide which is better approach to go from ahmedabad to delhi. 
# By car or by train. person has his own petrol car

car_distance = int(input("Enter Distance between ahmedabad to delhi by car : "))
petrol_price = int(input("Enter price of petrol : "))
cost_of_car = car_distance * petrol_price
print(f"Cost of Car : {cost_of_car}")

num_of_person = int(input("Enter number of person whose going to delhi by train : "))
train_ticket = int(input("Enter price of train ticket : "))
cost_of_train = num_of_person * train_ticket
print(f"Cost of Train :{cost_of_train}")

if cost_of_car < cost_of_train:
    print("Car is better approach to go from ahmedabad to delhi.")
else:
    print("Train is better approach to go from ahmedabad to delhi.")


 