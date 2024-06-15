n=list(input().split(' '))
x={}
for i in n:
    x[i]=n.count(i)
jishu=0
b=max(x.values())
c=[]
for i in x:
    if x[i]==b:
        c.append(i)
c.sort()
for i in c:
    print('{} {}'.format(i,jishu))
