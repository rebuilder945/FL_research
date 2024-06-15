a={}
lst=list(input().split( ))
lst.sort()
for x in lst:
    a[x]=lst.count(x)
for x in a:
    if a.get(x)==max(a.values()):
        print("{} {}".format(x,a.get(x)))

