n=eval(input())
i=2
m=1
lst=[]
lst1=[1,1]
for x in range(n):
    a=i/m
    lst.append(a)
    lst1.append(m)
    del lst1[0]
    i=i+m
    m=sum(lst1)
k=sum(lst)
print("%.4f"%(k))
