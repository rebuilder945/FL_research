def Fibonacci(num,  n):
    a,b=num[0],num[1]
    i=2
    while i<n:
        a,b=b,a+b
        i=i+1
    return(b)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


