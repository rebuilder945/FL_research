GDP={}
n=input() or 'ok'
while n !='ok':
    c,n=n.split()
    n=eval(n)
    GDP[c]=n
    n=input() or 'ok'
print(list(GDP.keys()))
print(sorted(list(GDP.values())))
if "India" not in list(GDP.keys()):
    print('no')
print(sum(list(GDP.values())))


