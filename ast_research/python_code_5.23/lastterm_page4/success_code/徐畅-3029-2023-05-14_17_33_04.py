def Fibonacci(num,  n,i):
    
    while n>2 and i<n-2:
        a=num[i]+num[i+1]
        num.append(a)
        Fibonacci(num,  n,i+1)
    return num[-1]
num  =  [1,  1]
i=0
n  =  int(input())
print(Fibonacci(num,  n,i))


    
