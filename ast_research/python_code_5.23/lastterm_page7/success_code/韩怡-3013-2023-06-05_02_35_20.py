GDP={}
while True:
    g=input()
    if g=='ok':
        break
    g=g.split()
    GDP[g[0]]=eval(g[1])
a=[]
b=[]
for i in GDP:
    a.append(i)
    b.append(GDP[i])
print(a.sort())
print(b.sort())
if 'India' in GDP:
    print('yes')
else:
    print('no')
print(sum(GDP.values()))

