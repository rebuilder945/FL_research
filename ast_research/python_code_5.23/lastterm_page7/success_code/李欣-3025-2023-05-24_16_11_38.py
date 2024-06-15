n=list(input().split( ))
ls=[]
for i in n:
    m=n.count(i)
    ls.append(m)
for i in n:
    if max(ls)==n.count(i):
        print(i,max(ls))
