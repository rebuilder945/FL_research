GDP={}
a=input()
while a!='ok':
    m,n=map(str,a.split())
    GDP[m]=int(n)
    a=input()
list1=[]
list2=[]
for i in GDP.keys():
    list1.append(i)
for j in GDP.values():
    list2.append(j)
list1.sort()
list2.sort()
print(list1)
print(list2)
if 'india' in GDP:
    print('yes')
else:
    print('no')
print(sum(list2))
