def Fibonacci(num,n):
    a=1
    b=1
    for i in range(n-2):
        a,b=b,a+b
        num.append(b)
    return(b)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


