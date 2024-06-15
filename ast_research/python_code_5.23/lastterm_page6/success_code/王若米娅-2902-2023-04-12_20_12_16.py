a=2
b=1
c=2/1
n=eval(input())
for x in range(n-1):
    n=a+b
    c+=n/a
    a,b=n,a
print("%.4f"%c)
        
   
   

