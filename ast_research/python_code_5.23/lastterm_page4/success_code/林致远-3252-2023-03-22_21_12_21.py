def Fibonacci(num,n):
    for x in range(n):
        l = len(num)
        number = num[l-1] + num[l-2]
        num.append(number)
    print(num[n-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


