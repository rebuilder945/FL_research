def Fibonacci(a,b):
    for i in range(n-2):
        a.append(a[-1]+a[-2])
    sum=a[-1]
    return sum
        
       




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


