h=eval(input())
n=eval(input())
b=h
for x in range(n):
    a=0.5*h
    b=b+2*a
    h=a
b=b-2*a
print("%.2f" %(b))
