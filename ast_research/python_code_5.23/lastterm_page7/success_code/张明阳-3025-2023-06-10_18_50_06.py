a=input()
y=[]
for q in a:
    s=a.count(q)
    y.append(s)
    t=max(y)
for i in range(len(a)):
    if t!=y[i]:
        continue
    k=a[i]
print(f'{k},{t}')
