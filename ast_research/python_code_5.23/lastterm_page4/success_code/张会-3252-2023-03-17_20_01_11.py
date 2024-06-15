def Fibonacci(num,  n):
    for i in range(n):
        if i >2:
             a =num[i-1] + num[i-2]
    return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


