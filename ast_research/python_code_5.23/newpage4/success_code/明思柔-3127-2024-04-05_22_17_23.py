n=int(input())
a=[x for x in range(1,n+1)]
b=a[0]
a.remove(b)
a.append(b)
print(a)
