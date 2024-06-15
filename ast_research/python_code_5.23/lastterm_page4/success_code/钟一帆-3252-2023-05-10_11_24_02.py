def Fibonacci(num,n):
    
    for i in range (n-2): 
        c=num[0]+num[1]
        num[0]=num[1]
        num[1]=c
    return num[1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


