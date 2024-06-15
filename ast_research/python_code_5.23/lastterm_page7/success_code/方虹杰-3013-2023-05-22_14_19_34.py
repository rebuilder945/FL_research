a={}
b=[]
c=[]
d=input()
while d!='ok':
    e,f=map(str,d.split(''))
    a[e]=int(f)
    d=input()
for i in a.keys():
    b.append(i)
for i in a.values():
    c.append()
b.sort()
c.sort()
print(b)
print(c)
if 'India' in a:
    print('yes')
else:
    print('no')
print(sum(c))
    

