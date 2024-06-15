GDP={}
while True:
    g=input()
    if g=='ok':
        break
    x,y=g.split()
    GDP[x]=eval(y)
a=[]
b=[]
for i in GDP:
    a.append(i)
    b.append(GDP[i])
a.sort()
b.sort()
print(a)
print(b)
if 'India' in GDP:
    print('yes')
else:
    print('no')
print(sum(GDP.values()))

