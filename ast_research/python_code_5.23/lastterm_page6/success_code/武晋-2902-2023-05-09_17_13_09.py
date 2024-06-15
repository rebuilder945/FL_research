def Fibonacci(n):
    if n<=2:
            return n
    return Fibonacci(n-1)+Fibonacci(n-2)
n= eval(input())    
res=0
for i in range(1,1+n):
    res+=Fibonacci(i+1)/Fibonacci(i)
print("%.4f"%res)
    



