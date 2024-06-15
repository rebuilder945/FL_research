from types import GetSetDescriptorType
dic={}
a=True
while a:
    b=input().split(' ')
    if b[0]=='ok':
        break
    else:
        dic[b[0]]=b[1]
keys=list(dic.keys())
values=list(dic.values())
values=list(int(i) for i in values)
keys.sort()
values.sort()
print(keys)
print(values)
if 'India' in dic:
    print('yes')
else:
    print('no')
print(sum(values))
