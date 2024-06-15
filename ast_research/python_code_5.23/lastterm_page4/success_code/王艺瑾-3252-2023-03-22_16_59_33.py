def Fibonacci(num,n):
    x=0
    while x<=n-2:
        num[0],num[1]=num[1],num[0]+num[1]
        x+=1
    return num[1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


