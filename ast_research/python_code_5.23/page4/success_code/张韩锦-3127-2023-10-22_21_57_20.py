n=eval(input())
lst=[i for i in range(1,n+1)]
lst2=[]
for k in lst:
    k=k+1
    lst2.append(k)
del lst2[-1]
lst2.append(1)
print(lst2)
