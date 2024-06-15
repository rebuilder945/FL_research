n=int(input())
lst=[x for x in range(1,n+1)]
a=lst[0]
lst.remove(a)
lst.append(a)
print(lst)



