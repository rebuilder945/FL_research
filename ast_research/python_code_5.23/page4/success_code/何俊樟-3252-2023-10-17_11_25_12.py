def Fibonacci(a,b):
    for x in range(b-2):
        c=sum(a)
        a.append(c)
        del a[0]
    return a[1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


