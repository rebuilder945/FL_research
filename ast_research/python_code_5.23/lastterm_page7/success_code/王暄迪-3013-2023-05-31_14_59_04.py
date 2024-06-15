GDP={}
a=input()
while a!='ok':
    a,b=map(str,a.split())
    GDP[a]=int(b)
    a=input()
lst1=[]
lst2=[]
for i in GDP.keys():
    lst1.append(i)
for i in GDP.values():
    lst2.append(i)
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
if 'India' in GDP:
    print('yes')
else:
    print('no')
print(sum(lst2))
