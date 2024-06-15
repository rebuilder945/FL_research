a=input().split(' ')
g={}
while a != ['ok']:
    g[a[0]]=a[1]
    a=input().split(' ')
c=[]
d=[]
for k,v in g.items():
    c.append(k)
    d.append(v)
c.sort()
d.sort()
if 'India' in g:
    print('yes')
else:
    print('no')
sum=0
for i in d:
    x=eval(i)
    sum+=x
print(sum)

