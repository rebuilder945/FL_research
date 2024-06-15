item=input()
n=[]
ls=[]
while item!='q':
    n.append(item)
for i in n:
    m=n.count(i)
    ls.append(m)
ls1=reversed(ls)
max=ls[0]
for i in n:
    while max==n.count(i):
        print(i,max)
