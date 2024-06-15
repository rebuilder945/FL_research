n=eval(input())
a=list(range(1,n+1))
b=a.copy()
for x in a:
	b[a.index(x)-1]=a[a.index(x)]
print(b)

