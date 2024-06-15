def Fibonacci(num,n):
    if n == 1 or n ==2:
        return(1)
    else:
        for x in range(n):
            if x == 0 or x == 1:
                num=num
            else:
                a = num[x-1]+num[x-2]
                num.append(a)
    return(num[n-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


