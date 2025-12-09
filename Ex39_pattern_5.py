'''
* * * * *
 * * * *
  * * *
   * *
    *
'''

row = 1

while row <=5:
    column = 1
    while column <= row:
        print('',end=' ')
        column+=1
    astrik = 6 - row
    star =1 
    while star<=astrik:
        print('*',end=' ')
        astrik-=1    
    print()
    row+=1
