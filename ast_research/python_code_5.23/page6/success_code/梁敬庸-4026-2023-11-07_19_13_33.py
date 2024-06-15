def line(n):
    a,b=2,1
    sum=0
    for x in range(n):
        sum+=a/b
        a,b=a+b,a
    return sum   
m=eval(input())
n=line(m)
print("%.4f"%n)

