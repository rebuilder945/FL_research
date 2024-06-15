s=input() or "ok"
lis_keys=[]
lis_values=[]
sums=0
while s!="ok":
    key,value=s.split()
    lis_keys.append(key)
    lis_values.append(value)
    s=input() or "ok"
lis_keys.sort()
lis_values.sort()
print(lis_keys)
for i in lis_values:
    i=int(i)
    sums+=i
print(lis_values)
if "India" in lis_keys:
    print('yes')
else:
    print('no')
print(sums)
