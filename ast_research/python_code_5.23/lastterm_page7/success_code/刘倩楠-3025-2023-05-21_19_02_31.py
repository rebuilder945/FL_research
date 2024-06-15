m=input().split()
m.sort()
n=[]
times=[]
for x in m:
    n.append(x,m.count(x))
    times.append(count(x))
n=dict(n)
for v,k in n:
    if k==max(times):
        print(v,k)
