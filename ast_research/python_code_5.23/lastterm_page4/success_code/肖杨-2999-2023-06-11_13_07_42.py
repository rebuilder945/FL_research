a=list(input().split())
b,c=input().split()
b=eval(b)
c=eval(c)
a[b],a[c] = a[c],a[b]
print(a)


