def Fibnacci(num,n):
    if n==1 or n==0:
        return 1
    else:
        return Fibnacci(num,n-1)+Fibnacci(num,n-2)





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


