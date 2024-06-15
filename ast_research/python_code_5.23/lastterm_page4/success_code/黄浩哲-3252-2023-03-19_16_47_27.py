def Fibonacci(num,  n):
    a,b=1,1
    count=0
    while(count!=n-2):
        a,b=b,a+b
        count+=1
    return b
    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


