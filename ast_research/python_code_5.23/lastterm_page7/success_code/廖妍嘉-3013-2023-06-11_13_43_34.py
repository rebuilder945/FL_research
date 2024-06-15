GDP={}
n=input() or 'ok'
while n !='ok':
    c,n=n.split()
    n=eval(n)
    GDP[c]=n
    n=input() or 'ok'
print(sorted(list(GDP.keys())))
print(sorted(list(GDP.values())))
if "India" not in list(GDP.keys()):
    print('no')
else:
    print('yes')
print(sum(list(GDP.values())))


