t=input()
t=t.replace("[","").replace("]","")
t=t.split(',')
t=list(map(int,t))
p=[]
q=[]
for i in t:
    for x in range(2,i//2+1):
        if i%x==0:
            p.append(i)
for x in t:
    if x not in p:
        q.append(x)
for y in q:
    if y==1:
        q.remove(1)
print(q)


