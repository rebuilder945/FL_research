x = 2
y = 1
sum = 0
n = eval(input())
while n > 0:
    sum = sum + x/y
    m = y
    y = x
    x = x + m
    
    n = n-1
print("%.4f"%sum)
