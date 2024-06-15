n=eval(input())
lst=[x for x in range (1,n+1,1)]
b=lst[0]
del lst[0]
lst.insert(n-1,b)
print(lst)
