n=eval(input())
lst=[x for x in range(1,n+1)]
m=lst[0]
lst.pop(0)
lst.append(m)
print(lst)
