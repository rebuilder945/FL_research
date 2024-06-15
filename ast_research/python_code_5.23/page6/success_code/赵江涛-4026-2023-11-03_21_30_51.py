n = eval(input())
s = 0
x = 2
y = 1
while n>0:
    s = s+x/y
    a = x
    y = a+y
    b = x+y
    x = a+b
    n-=1
print(s)    
