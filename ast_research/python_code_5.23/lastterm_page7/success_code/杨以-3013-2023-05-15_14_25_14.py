ls1=[]
ls2=[]
while 1:
    s=input()
    if s!='ok':
        n,m=s.split(' ')
        ls1.append(n)
        ls2.append(int(m))
    elif s=='ok':
        break
di=dict(zip(ls1,ls2))
key=sorted(list(di.keys()))
value=sorted(list(di.values()))
print(key)
print(value)
if 'india' in key:
    print('yes')
elif 'inida' not in key:
    print('no')
print(type(value[0]),type(value[1]),type(value[2]))
print(sum(value))
print(di)
    
    
