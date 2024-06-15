n=eval(input())
lst=[]
a=[2,3]
b=[1,2]
for i in range(n):
    a.append(a[i]+a[i+1])
    b.append(b[i]+b[i+1])
    x=a[i]/b[i]
    lst.append(x)
num=sum(lst)
print("%.4f"%(num))
