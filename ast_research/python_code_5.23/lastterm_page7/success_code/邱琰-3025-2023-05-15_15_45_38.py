m=input().split(" ")
m.sort
n=[]
times=[]
for i in m:
    n.append((i,m.count(i)))
    times.append(m.count)
n=dict(n)
for k,v in n.items():
    if v==max(times):
        print(k,v)
