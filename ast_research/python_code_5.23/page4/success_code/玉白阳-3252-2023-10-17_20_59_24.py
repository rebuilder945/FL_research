def Fibonacci(n):
    num_list=[1,1]
    for i in range (2,n):
        num_list.append(num_list[-1]+num_list[-2])
    return fib_list




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


