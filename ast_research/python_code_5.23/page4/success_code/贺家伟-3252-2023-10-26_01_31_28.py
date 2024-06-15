def Fibonacci(num,n):
    for i in range(n):
        num.append(num[i]+num[i+1])    
    return num[-3]
        




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


