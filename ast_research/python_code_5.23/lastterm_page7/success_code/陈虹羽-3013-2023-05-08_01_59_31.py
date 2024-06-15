a=input().split()
GDP={}
key=[]
value=[]
while a[0]!='ok':
    GDP[a[0]]=int(a[1])
    a=input().split()
for k,v in GDP.items():
    key.append(k)
    value.append(v)
key.sort()
value.sort()
print(key)
print(value)
if "India" in GDP:
    print('yes')
else:
    print("no")
print(sum(value))


