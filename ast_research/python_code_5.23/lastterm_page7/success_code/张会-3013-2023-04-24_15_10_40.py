s=input() or 'ok'
m={}
ls1=[]
ls2=[]
while(s!='ok'):
    b=s.split()
    m[b[0]]=b[1]
    s=input() or 'ok'
for i in m:
    ls1.append(i)
ls1.sort()
print(ls1)
for k,v in m.items():
    v1=eval(v)
    ls2.append(v1)
ls2.sort()
print(ls2)
if 'India' in m:
    print('yes')
else:
    print('no')
sum=sum(ls2)
print(sum)
