def  Fibonacci(a,i):
    a=1
    b=2
    for x in range(i-2):
        c=a+b
        a=b
        b=c
    return(c)
a=[1,2]
n=eval(input())
d=[]
for i in range(n):
    m=Fibonacci(i+2)/Fibonacci(i+1)
    d.append(m)
e=sum(d)
print("%.4f"%e)



