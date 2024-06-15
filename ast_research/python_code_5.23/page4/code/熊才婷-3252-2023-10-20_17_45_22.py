 def Fibonacci(ls,n):
    ls=[1,1]
    n=n-2
    for i in range(n):
        x=ls[-1]+ls[-2]
        ls.append(x)
    a=ls[-1]
    return a





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


