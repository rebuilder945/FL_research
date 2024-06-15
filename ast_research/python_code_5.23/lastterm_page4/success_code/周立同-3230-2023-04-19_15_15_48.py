lst=eval(input())
lst1=lst.copy()
lst2=[]
for i in range(0,len(lst1)):
    k=max(lst)
    q=len(lst)-1
    lst2.append(k*(10**q))
    lst.remove(k)
he=sum(lst2)
print(he)
