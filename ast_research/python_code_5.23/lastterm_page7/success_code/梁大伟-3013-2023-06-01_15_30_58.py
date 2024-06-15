gdp={}
a=input() or 'ok'
while a!='ok':
    b=a.split()
    gdp[b[0]]=eval(b[1])
    a=input() or 'ok'
ky=[]
val=[]
kv=[]
for k,v in gdp.items():
    kv.append([k,v])
kv.sort(key=lambda x:x[1])
for n in kv:
    ky.append(n[0])
for m in kv:
    val.append(m[1])
print(ky)
print(val)
if 'India' in gdp:
    print('yes')
else:
    print('no')
print(sum(val))
