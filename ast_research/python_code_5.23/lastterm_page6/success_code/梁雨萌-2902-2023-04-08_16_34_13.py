def Fibonacci(num,  n):
    for i in range(1,n+1):
        x=num[i-1]+num[i]
        num.append(x)
    return num
    
num  =  [1,  1]
n  =  int(input())
Fibonacci(num,  n)
list=[]
for i in range(1,n+1):
    list.append(num[i+1]/num[i])
print("%.4f"%(sum(list)))
