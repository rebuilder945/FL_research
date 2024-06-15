n=int(input())
lst=[x for x in range(1,n+1,1)]
a=lst[0]
lst1=lst.append(a)
lst2=lst1.pop(0)
print(lst2)
