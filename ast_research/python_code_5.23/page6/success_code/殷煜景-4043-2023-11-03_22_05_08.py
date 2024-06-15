lst1=eval(input())
m=[]
n=[]
for i in lst1:
    for x in i:
        if x not in m:
            m.append(x)
            n.append(x)
        else:
            n.append(x)
m.sort(reverse=False)
for i in m:
    q=n.count(i)
    print(i,q)
