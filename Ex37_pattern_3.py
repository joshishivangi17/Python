'''
    1
   21
  212
 1212
12121

'''

row = 1
num = 5

while row <= 5:
    space = 0
    while space < (num - row):
        print("  ", end="")
        space += 1

    column = 1
    while column <= row:
        if column%2 == 1:
            print('1',end=' ')
        else:
            print('2',end=' ')
        column+=1
    print()
    row+=1
 