def Fibonacci(num,n) :
    if n<2 :
        return n
    else :
        return Fibonacci(n-1)+Fibonacci(n-2)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


