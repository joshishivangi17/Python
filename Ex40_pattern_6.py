'''    
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''

row = 1
num = 5

while row <= num:
    column = 1
    while column<= num-row:
        print('  ',end='')
        column+=1
    astrik = 1
    while astrik<=row:
        print('* ',end='')
        astrik+=1
    
    print()
    row+=1
    
row = num - 1
while row >=1:
    column = 1
    while column<=num-row:
        print('  ',end='')
        column+=1
    astrik = 1
    while astrik <= row:
        print('* ',end='')
        astrik+=1
    print()
    row -=1