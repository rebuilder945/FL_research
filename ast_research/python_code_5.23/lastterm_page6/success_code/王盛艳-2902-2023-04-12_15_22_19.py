x = 2
y = 1
n = int(input())
sum = 0
while n>0:
    sum += x/y
    m = y
    y = x
    x += m
    n -= 1
print("%.4f"%sum)
