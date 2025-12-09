'''

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

'''

row = 5

while row >= 1:
    column = 1
    num = row
    while column <= row:
        print(f"{num}",end=' ')
        num-=1
        column+=1
    print()
    row-=1