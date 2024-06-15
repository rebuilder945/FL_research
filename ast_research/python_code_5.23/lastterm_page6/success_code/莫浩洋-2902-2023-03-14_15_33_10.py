
def Fibonacci(n):
    listf=[]
    a=1  
    b=0  
    c=1
    for i in range (n+1):
        c=a+b
        listf.append(c)
        b=a
        a=c
    
    return listf
n  =  int(input())
listf=Fibonacci(n)
d=0
for i in range (n):
    d+=listf[i+1]/listf[i]
print("%.4f"%d)
