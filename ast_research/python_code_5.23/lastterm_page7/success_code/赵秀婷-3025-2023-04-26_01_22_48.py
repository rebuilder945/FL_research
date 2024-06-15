m=input().split(" ")
m.sort()
n=[]
times=[]
for x in m:
    n.append((x,m.count(x)))
    times.append(m.count(x))
n=dict(n)
for k,v in n.items():
    if v == max(times):
        print(k,v)
