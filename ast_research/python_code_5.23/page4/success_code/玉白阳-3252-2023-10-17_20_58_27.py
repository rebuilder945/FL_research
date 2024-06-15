def Fibonacci(n):
    fib_list=[1,1]
    for i in range (2,n):
        fib_list.append(fib_list[-1]+fib_list[-2])
    return fib_list




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


