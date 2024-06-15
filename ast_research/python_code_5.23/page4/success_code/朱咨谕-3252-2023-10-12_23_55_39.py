def Fibonacci(a,b):
    b-=1
    #1,1,2,3,5,8,13
    #0 1 2 3 4 5 6
    if(b==0 or b==1) :
        return a[b]
    else : 
        for i in range(2,b+1):
            a.append(a[i-1]+a[i-2])
        return a[b]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


