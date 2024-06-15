def Fibonacci(num,n):
    a,b=1,1
    c=0
    while(c!=n-2):
        a,b=b,a+b
        c+=1
    return b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


