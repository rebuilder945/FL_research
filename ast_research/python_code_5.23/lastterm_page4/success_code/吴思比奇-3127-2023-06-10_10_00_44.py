n=eval(input())
a=[x for x in range(1,n+1)]
q=a[0]
e=a[-1]
a[0]=e
a[-1]=q
print(a)
