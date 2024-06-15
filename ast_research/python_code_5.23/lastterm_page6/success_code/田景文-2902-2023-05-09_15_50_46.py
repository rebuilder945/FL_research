n = int(input())
x = 2
y = 1
s = 0
i = 0
while i<n:
    s+=x/y
    x,y=x+y,x
    i+=1
print("%.4f"%s)
