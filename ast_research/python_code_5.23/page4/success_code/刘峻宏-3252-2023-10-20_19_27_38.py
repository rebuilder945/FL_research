def Fibonacci(num,n):
    if n>2:
        for i in range(n-2):
            s=num[i]+num[i+1]
            num.append(s) 
    else:
        pass        
    d=num[-1]
    return d




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


