a=input().split(' ')
g={}
while a != ['ok']:
    g[a[0]]=a[1]
    a=input().split(' ')
c=[]
d=[]
e=[]
for k,v in g.items():
    c.append(k)
    d.append(v)
c.sort()
d.sort()
print(c)
sum=0
for i in d:
    x=eval(i)
    sum+=x
    e.append(x)
print(e)
if 'India' in g:
    print('yes')
else:
    print('no')
print(sum)

