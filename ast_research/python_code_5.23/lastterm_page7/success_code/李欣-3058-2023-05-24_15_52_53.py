item=input()
n=[]
ls=[]
while item!='q':
    n.append(item)
for i in n:
    m=n.count(i)
    ls.append(m)
for i in n:
    if max(ls)==n.count(i):
        print(i,max)
        break
