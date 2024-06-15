def Fibonacci(num,n):
    num=[1,1]
    for i in range(n-2):
        num.append(int(num[-1])+int((num[-2])))
    return(num[n-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


