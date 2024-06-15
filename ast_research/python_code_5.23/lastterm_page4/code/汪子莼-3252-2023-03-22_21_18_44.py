def Fibonacci(num,n):
    for i x in range(3,n+1):
        m=sum(num[x-3:x-1])
        num.append(m)
    return max(num)
       




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


