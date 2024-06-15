def Fibonacci(num,n):
    if n==1:
        x=1
    elif n==2:
        x=1
    elif n>2:
        x=Fibonacci(num,  n-1)+Fibonacci(num,  n-2)
    return x




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


