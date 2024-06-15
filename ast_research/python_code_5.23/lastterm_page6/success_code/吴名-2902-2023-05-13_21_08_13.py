def n(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return(a)
x=eval(input())
a=0
for i in range(x):
    a+=n(i+3)/n(i+2)
print("%.4f"%a)
