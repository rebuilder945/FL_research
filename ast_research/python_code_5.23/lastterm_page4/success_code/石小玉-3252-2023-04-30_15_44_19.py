def Fibonacci(num,n):
    
    while  n:
        x = num[-2]+num[-1]
        num.append(x)
        
    result=num[n-1]
    return result




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


