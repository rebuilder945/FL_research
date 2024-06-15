dit={}
lst1=[]
lst2=[]
while True:
    a,b=input().split()
    if a!='ok':
        dit[a]=b
        lst1.append('a')
        lst2.append(int(b))
    else:
        break
print(lst1)
print(lst2)
if 'India' in dit.items():
    print('yes')
else:
    print('no')
print(sum(lst2))
