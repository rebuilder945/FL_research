def Fibonacci(num,  n):
    for i in range(n-2):
        num.append(num[i]+num[i+1])
    a=0
    for i in num:
        a+=int(i)
return(a)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


