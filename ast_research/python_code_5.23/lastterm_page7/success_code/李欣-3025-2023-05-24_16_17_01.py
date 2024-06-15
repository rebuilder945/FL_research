n=list(input().split( ))
ls=[]
for i in n:
    m=n.count(i)
    ls.append(m)
ls1=[]
for i in n:
    if i not in ls1:
        ls1.append(i)
for a in ls1:
    if max(ls)==n.count(a):
        print(a,max(ls))
