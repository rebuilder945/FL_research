h = eval(input())
N = eval(input())
x = h
n = 1
m = 0
while n < N:
    m = 2*h*(0.5)**n
    n += 1
    x += m
print("%.2f"%x)    



