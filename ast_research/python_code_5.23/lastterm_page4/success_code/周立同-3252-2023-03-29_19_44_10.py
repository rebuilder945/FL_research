def Fibonacci(num,  n):
    num=[1,1]
    for i in range(1,n-2):
        num.append(num[-1]+num[-2])
    return num[-2]+num[-1]
num  =  [1,  1]
n  =  int(input())




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


