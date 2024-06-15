n=eval(input())
lst=[1,2]
lst1=[1]
for a in range(2,n):
    b=lst[a-1]+lst[a-2]
    lst.append(b)
for x in range(n-1):
    c=lst[x]/lst[x+1]
    lst1.append(c)
d=sum(lst1)+n
print("%.4f"%(d))
    


