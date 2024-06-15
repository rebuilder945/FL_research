n = eval(input())
lst=[x for x in range(1,n+1)]
lst1=lst.copy()
lst.remove(lst[0])
lst.append(lst1[0])
print(lst)

