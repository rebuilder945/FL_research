def Fibonacci(a,b):
    for x in range(b):
        c=a.sum()
        a.append(c)
        del c[0]
print(a[1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


