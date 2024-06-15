def Fibonacci(num,n):
    n3=1
    n1=num[0]
    n2=num[1]
    while (n-2)>0:
        n3=n2+n1
        n1=n2
        n2=n3
        n-=1
    return n3




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


