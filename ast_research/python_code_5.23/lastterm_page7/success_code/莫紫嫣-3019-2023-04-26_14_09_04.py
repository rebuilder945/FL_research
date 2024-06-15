a=input()
a=a.split('')
d={}
d['name']=a[0]
d['english']=int(a[1])
d['python']=int(a[2])
d['math']=int(a[3])
f=list(d.values())
h=f.copy()
for i in f:
    if type(i)!=int:
        h.remove(i)
h.sort(reverse=True)
print(a[0],'%.2f'%(h[0]),'%.2f'%(h[1]),'%.2f'%(h[2]),'%.2f'%(h[3]))

