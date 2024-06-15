d={}
while True:
    n=input()
    if n=='ok':
        break
    else:
        lst=n.split(' ')
        d[lst[0]]=int(lst[1])
lst1=list(d.keys())
lst2=list(d.values())
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
if 'India' in lst1:
    print("yes")
else:
    print("no")
print(sum(lst2))
