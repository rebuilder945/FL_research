def Fibonacci(num,  n):
    for i in range(1,n+1):
        x=num[i-1]+num[i]
        num.append(x)
    word=num[n-1]
    return(word)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


