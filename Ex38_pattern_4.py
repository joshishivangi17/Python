''' 
    1
   2 3
  4 5 6
 7 8 8 10
 '''

row = 1
num = 1

while row <= 4:
    space = 4 - row
    column = 0
    while column < space:
        print('',end=' ')
        column +=1

    numbers_in_row = row
    column = 0
    while column < numbers_in_row:
        print(f"{num}",end=' ')
        num +=1
        column +=1    
    print()
    row+=1
    
