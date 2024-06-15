n=eval(input())
a=[i for i in range(n)]
for i in a:
    m=a.index('i')
    m-=1
    del a[i]
    a.insert(m,'i')
print(a)
