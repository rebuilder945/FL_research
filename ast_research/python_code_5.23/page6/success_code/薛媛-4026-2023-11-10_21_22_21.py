def  Fibonacci(a,n):
    a=1
    b=2
    for x in range(n-2):
        c=a+b
        a=b
        b=c
    print(c)
a=[1,2]
n=int(input())
d=[]
for i in range(n):
    m=Fibonacci(a,i+2)/Fibonacci(a,i+1)
    d.append(m)
e=sum(d)
print("%.4f"%e)




