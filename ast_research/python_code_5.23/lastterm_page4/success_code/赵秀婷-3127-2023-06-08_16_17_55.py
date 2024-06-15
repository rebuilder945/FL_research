n=eval(input())
lst=[x for x in range(1,n+1)]
a=lst[0]
del lst[0]
lst.append(a)
print(lst)
