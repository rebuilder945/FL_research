def Fibonacci(num,  n):
    num  =  [1,  1]
    for i in range(n-2):
        num.append(num(i)+num(i+1))
    return num




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


