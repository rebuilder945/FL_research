e=input()
m=[x for x in e]
x=m.copy
n=[]
p=[]
if len(m)==0:
    print("None")
else:
    for i in m:
        if m.count(i)>1:
            n.append(i)
    for i in m:
        if i not in n:
            p.append(i)
    print(p[0])
