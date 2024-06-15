def Fibonacci(num,n):
    last=num[0]
    now=num[1]
    next=num[1]
    for i in range(n):
        if i <2:
            next=1
        else:
            next=last+now
            last=now
            now=next
    return next




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


