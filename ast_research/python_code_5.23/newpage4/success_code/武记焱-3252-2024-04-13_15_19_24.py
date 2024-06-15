def fibonacci(num,n):
        num=[1,1]
        for _ in range(3, n + 1):
            num[0],num[1]=num[1],num[0]+num[1]
        return num[1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


