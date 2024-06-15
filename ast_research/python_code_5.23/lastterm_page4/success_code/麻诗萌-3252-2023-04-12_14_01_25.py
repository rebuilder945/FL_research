def Fibonacci(num,n) :
    for i in range(n) :
        if i >1 :
            m=num[i-1]+num[i-2]
            num.append(m)
        else:
            num[n]=1
    return num[n]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


