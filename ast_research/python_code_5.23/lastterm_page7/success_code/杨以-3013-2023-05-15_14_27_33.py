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
if 'India' in key:
    print('yes')
elif 'Inida' not in key:
    print('no')
print(sum(value))
print(di)
    
    
