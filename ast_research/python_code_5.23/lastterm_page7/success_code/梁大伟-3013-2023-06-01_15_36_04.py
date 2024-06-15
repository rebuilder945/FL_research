gdp={}
a=input() or 'ok'
while a!='ok':
    b=a.split()
    gdp[b[0]]=eval(b[1])
    a=input() or 'ok'
ky=[]
val=[]
for k,v in gdp.items():
    ky.append(k)
    val.append(v)
ky.sort()
val.sort()
print(ky)
print(val)
if 'India' in gdp:
    print('yes')
else:
    print('no')
print(sum(val))
