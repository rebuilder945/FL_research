n=eval(input())
lst=[x for x in range(1,n+1)]
lst.insert(len(lst),lst[0])
del lst[0]
print(lst)
