def Fibonacci(num,  n):
    a=sum(num)
    num=[num[1],a]
    return sum(num)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


