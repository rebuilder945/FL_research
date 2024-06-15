from cmath import pi


dict={}
while True:
    n=input()
    if n=='ok':
        break
    else:
        lst=n.split()
        dict[lst[0]]=int(lst[1])
lst1=list(dict.keys())
lst2=list(dict.values())
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
if 'India' in dict:
    print('yes')
else:
    print('no')
print(sum(lst2))
