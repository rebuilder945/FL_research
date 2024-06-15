s=input().split()
d={}
while 'ok' not in s:
    d[s[0]]=s[1]
    s=input().split()
ls1=list(d.keys())
print(ls1)
ls2=list(d.values())
ls3=list(map(int,ls2))
print(ls3)
if 'india' in ls2:
    print('yes')
else:
    print('no')
print(sum(ls3))
