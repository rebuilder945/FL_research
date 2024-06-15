a=eval(input())
n=1
m=n
lst=[]
for i in range(a):
    n,m=m,n+m
    lst.append(m/n)
x=sum(lst)
print("%.4f"%x)
