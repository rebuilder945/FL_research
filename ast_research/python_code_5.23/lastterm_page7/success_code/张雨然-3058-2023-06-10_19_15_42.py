lst=[]
i=input()
while i!="q":
    lst.append(i)
    i=input()
n=[]
times=[]
for x in lst:
    n.append((x,lst.count(x)))
    times.append(lst.count(x))
n=dict(n)
for k,v in n.items():
    if v == max(times):
        print(k,v)
