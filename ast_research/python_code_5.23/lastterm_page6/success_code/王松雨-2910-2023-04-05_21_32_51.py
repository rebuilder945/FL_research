h=eval(input())
n=eval(input())
s=h
for i in range(1,n+1):
    h=h*0.5
    s+=2*h
print("%.2f"%s)

