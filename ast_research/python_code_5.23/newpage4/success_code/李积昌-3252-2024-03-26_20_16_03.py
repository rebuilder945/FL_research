def Fibonacci(num,n) :
    if n==1 :
        return n
    elif n==2 :
        return n-1
    else :
        return Fibonacci(num,n-1)+Fibonacci(num,n-2)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


