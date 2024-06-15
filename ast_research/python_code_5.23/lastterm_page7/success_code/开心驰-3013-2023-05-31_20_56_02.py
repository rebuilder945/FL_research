a=input().split()
d={}
while a[0]!='ok':
    d[a[0]]=a[1]
    a=input().split()
lst1=list(d.keys())
lst2=list(map(int,d.values()))
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
if 'India' not in d:
    print('no')
else:
    print('yes')
print(sum(map(int,d.values())))
