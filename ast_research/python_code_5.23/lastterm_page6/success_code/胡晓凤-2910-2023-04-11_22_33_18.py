h=eval(input())
n=eval(input())
s=h
for i in range(n-1):
    s=s+h*(0.5)**(i)
s="%.2f"%s
print (s)
