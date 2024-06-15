n=eval(input())
lst=list(range(n+1))
k=lst[0]
lst.remove(k)
lst.append(k)
print(lst)
