def Fibonacci(num,  n):
    for x in Fibonacci(num):
        Fibonacci[x+2]=Fibonacci[x+1]+Fibonacci[x]
        return Fibonacci[num]
    return Fibonacci[n]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


