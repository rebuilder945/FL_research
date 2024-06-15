def Fibonacci(num,n):
    last=num[0];
    now=num[1];
    f=1 
    for i in range(n):
        if i<2:
              f=1
        else:
            f=now+last
            last=now
            now=f
    return f




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


