def Fibonacci(a,b):
    n1,n2=eval(a)
    c=1
    now=0
    while c<=n-2:
        now=n1+n2
        n1=n2
        n2=now
        c+=1
    return now





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


