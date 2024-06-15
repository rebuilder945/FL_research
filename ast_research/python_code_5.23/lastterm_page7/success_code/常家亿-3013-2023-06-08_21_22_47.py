a = input()or'ok'
GDP={}
while a!= 'ok':
    b = a.split()
    GDP[b[0]]=b[1]
    a = input() or 'ok'
lst1=list(GDP.values())
lst1.sort()
lst2=list(GDP.keys())
lst2.sort()
lst3=list(map(int,lst1))
print(lst2)
print(lst3)
if 'India' in GDP:
    print('yes')
else:
    print('no')
print(sum(lst3))

