n=eval(input())
lst=[i for i in range(1,n+1)]
a=lst[0]
lst.pop(0)
lst.insert(n,a)
print(lst)
