n=int(input())
lst=[x for x in range(1,n+1,1)]
a=lst[0]
lst.append(a)
lst.pop(0)
print(lst)
