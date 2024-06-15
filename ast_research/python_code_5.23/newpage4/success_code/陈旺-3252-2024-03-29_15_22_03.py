def Fibonacci(num,n):
    i=2
    while i<n:
        num.append(num[i-2]+num[i-1])
        i+=1
    return(num[-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


