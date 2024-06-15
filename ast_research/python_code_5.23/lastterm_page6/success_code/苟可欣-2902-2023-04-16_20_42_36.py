n=eval(input())
i=2
m=1
lst=[]
for x in range(n):
    a=i/m
    lst.append(a)
    m=m+1
    i=i+1
k=sum(lst)
print("%.4f"%(k))
