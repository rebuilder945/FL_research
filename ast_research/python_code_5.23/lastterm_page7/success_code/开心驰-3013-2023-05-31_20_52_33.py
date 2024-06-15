a=input().split()
d={}
while a[0]!='ok':
    d[a[0]]=a[1]
    a=input().split()
print(list(d.keys()).sort())
print(list(d.values()).sort())
if 'India' not in d:
    print('no')
print(sum(map(int,d.values())))
