n=eval(input())
lst=[]
a=2
m=1
for i in range(1,n+1):
    x=a/m
    lst.append(x)
    a,m=a+m,a
print("%.4f"%sum(lst))


    
