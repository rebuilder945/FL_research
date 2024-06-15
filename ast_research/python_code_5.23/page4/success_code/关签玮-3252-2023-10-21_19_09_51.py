def Fibonacci(ls,a):
    for i in range(a-2):
        b=ls[-1]+ls[-2]
        ls.append(b)
    return(ls[-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


