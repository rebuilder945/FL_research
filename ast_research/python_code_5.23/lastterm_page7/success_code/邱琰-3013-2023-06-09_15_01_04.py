dic={}
ls1=[]
ls2=[]
while 1:
    n=input()
    if n=='ok':
        break
    key,value=list(n.split())
    dic[key]=int(value)
    ls1.append(key)
    ls2.append(int(value))
print(ls1)
print(ls2)
if 'India' in ls1:
    print('yes')
else:
    print('no')
print(sum(ls2))
