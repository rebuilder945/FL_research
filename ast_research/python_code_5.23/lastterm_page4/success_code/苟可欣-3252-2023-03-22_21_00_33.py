def Fibonacci(num,n):
    Fi=num
    for x in range(2,n+1):
        a=sum(Fi[x-2:x])
        Fi.append(a)
    return max(Fi)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


