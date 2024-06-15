def flower(x):
    m=0
    a=[i for i in str(x)]
    s=0
    for t in a:
        s=s+(int(t))**3
    if s==int(x) and len(a)==3:
        m=1
    return m
n=eval(input())
a1=[]
for x in range(n+1):
    if flower(x):
        a1.append(x)
if a1==[]:
    print('none')
else:
    for x in a1:
        print(x)
