GDP={}
while True:
    a=input()
    if a=='ok':
        break
k,v=a.split(' ')
GDP[k]=int(v)
key=list(GDP.keys())
valuse=list(GDP.values())
key.sort()
valuse.sort()
print(key)
print(valuse)
print('yes'if 'India' in key else 'no')
print(sum(valuse))
