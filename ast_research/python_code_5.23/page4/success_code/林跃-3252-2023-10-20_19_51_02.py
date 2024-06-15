def Fibonacci(num,n):
    int1,int2=1,1
    for i in range(n-1):
        int1,int2=int2,int1+int2
        num=int2
    return num
        




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


