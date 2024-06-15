def Fibonacci(a,b):
    if b<=1:
        return 1
    elif b==2:
        return 1
    else:
        return Fibonacci(a,b-1)+Fibonacci(a,b-2)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


