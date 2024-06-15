def Fibonacci(a,b):
    for x in range(b):
        e=a[-1]+a[-2]
        a.append(e)
    return(a[-3])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


