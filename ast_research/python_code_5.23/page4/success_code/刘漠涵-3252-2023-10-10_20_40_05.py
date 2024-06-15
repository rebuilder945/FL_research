def Fibonacci(num,n):
    num=list(num)
    i=2
    while i<n :
        i+=1
        a=sum(num[-1:-3:-1])
        num.append(a)
    return(a,i)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


