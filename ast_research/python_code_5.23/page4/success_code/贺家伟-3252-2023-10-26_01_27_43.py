def Fibonacci(num,n):
    for i in range (n-2):
        num.append(num[i-1]+num[i-2])    
    return num[-4]
        




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


