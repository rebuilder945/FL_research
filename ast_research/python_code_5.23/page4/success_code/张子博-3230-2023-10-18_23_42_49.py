p=eval(input())
k=max(p)
n=min(p)
if k==n:
    print(k)
else:
    for i in range(len(p.copy())):
        l=max(p)
        print(l,end='')
        p.remove(l)
