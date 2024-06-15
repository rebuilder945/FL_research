def Fibonacci(a,  b):
    for x in range(1,b):
        a.append(a[x-1]+a[x-2])
    return(a[-1])





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


