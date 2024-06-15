def Fibonacci(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        print(b)
        a,b = b,a+b
        i = i+1
return(n)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


