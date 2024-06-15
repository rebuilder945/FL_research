t=input()
t=t.replace("[","").replace("]","")
t=t.split(',')
t=list(map(int,t))
p=[]
q=[]
for i in t:
    if i==2:
        q.append(i)
for i in t:
    for j in range(2,i):
        if i%j==0:
            pass
        else:
            p.append(i)
for i in p:
    if i not in q:
        q.append(i)
print(q)

