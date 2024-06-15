n = eval(input())
s = 0
x = 2
y = 1
while n>0:
    s = s+x/y
    a = y
    y = x
    x = x+a
    n-=1
print("%.4f"%s)    


