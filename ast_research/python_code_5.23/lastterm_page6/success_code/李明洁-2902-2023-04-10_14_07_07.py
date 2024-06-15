x = 2
y = 1
n = int(input())
sum = 0
while n>0:
    sum = sum+x/y
    m = y
    y = x
    x = x+m
    n -= 1
print("%.4f"%sum)
