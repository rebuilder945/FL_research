def Fibonacci(num,  n):
    num=[1,1]
    for x in range(1,n+1):
        num.append(num[x-1]+num[x])
    return(num[n-1])
num=[1,1]
n=int(input())
print(Fibonacci(num,n))




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


