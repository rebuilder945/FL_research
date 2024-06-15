m=input().split()
n=[]
times=[]
for x in m:
    n.append(x,m.count(x))
    times.append(count(x))
n=dict(n)
for k,v in n:
    if k==max(times):
        print(v,k)
