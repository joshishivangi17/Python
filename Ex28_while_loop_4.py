# 4)   0    1   1   2   3   5   8   13  .... 100

a = 0
b = 1
while a <= 100:
    print(a,end=' ')
    a, b = b, a + b
