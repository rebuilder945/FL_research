def Fibonacci(num,n):
    if n==0:
        return 0
    elif n==1:
        return 1
    numfn1=0
    numfn2=1
    for i in range(2,n+1):
        currentNum=numfn1+numfn2
        numfn1=numfn2
        numfn2=currentNum
    return currentNum

    





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


