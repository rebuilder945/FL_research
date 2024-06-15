s=list(input().split(' '))
a={}
for i in s:
    if i=='q':
        break
    else:
        a[i]=s.count(i)
b=[]
ll=max(a.values())
for i in a:
    if a[i]==ll:
        b.append(i)
for i in b:
    print("{} {}".format(i,ll))


