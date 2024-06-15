def Fibonacci(num,n):
    a1,a2=num
    for i in range(n-2):
        a3=a1+a2
        a1=a2
        a2=a3
    return(a3)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


