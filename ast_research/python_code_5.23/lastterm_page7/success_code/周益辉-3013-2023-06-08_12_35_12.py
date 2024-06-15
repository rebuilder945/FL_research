lst1=input().split()
dic1={}
while lst1!=['ok']:
    dic1[lst1[0]]=int(lst1[1])
    lst1=input().split()
lst2=list(dic1.keys())
lst3=list(dic1.values())
lst2.sort()
lst3.sort()
print(lst2)
print(lst3)
if 'India' not in dic1:
    print('no')
else:
    print('yes')
print(sum(lst3))
