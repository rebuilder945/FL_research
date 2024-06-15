def Fibonacci(a,b):
    sum=0
    for i in range(n-2):
        a.append(a[-1]+a[-2])
    for y in a:
        sum+=y
    return sum
        
       




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


