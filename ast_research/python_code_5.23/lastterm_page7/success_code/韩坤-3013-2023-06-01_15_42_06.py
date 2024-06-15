a={}
b=[]
c=[]
while True:
    x=input()
    if x=='ok':
        break
    x=x.split('')
    a[x[0]]=eval(x[1])
for x in a:
    b.append(x)
    c.append(a[x])
b.sort()
c.sort()
print(b)
print(c)
if 'India' in a:
    print('yes')
else:
    print('no')
print(sum(list(a.values())))
