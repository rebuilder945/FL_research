from os import rename


def Fibonacci(num,n):
    sk=num
    sk=list(sk)
    sk.pop()
    n=int(n)
    d=1
    x=0
    for d in range(n+1):
        x=x+sk[d-1]
        d=d+1
        sk.append(x)
        return sk[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


