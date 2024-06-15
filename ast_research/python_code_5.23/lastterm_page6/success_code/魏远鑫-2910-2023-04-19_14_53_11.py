h=eval(input())
n=eval(input())
l=h
for i in range(1,n):
    h*=0.5
    l+=2*h
print("%.2f"%l)

