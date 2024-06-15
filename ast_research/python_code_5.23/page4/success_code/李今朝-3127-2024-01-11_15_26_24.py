a=int(input())
lst=[x for x in range(1,a+1)]
lst2=lst.copy()
for x in range(a-1):
    lst2[x]=lst[x+1]
lst2[a-1]=lst[0]
print(lst2)
