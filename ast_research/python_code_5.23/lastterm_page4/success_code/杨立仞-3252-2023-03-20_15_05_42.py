def Fibonacci(a,b):
    for x in range(b-2):
        a.append(sum(a[x:x+2]))
    return a[b]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


