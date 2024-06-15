x = 2
y = 1
n = eval(input())
sum = 0
while n > 0:
    sum = sum+x/y
    a = x
    x = x+y
    y = a
    n -=1
print("%.4f"%sum)
