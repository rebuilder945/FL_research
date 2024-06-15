s=input().split()
d={}
while 'ok' not in s:
    d[s[0]]=s[1]
    s=input().split()
ls1=list(d.keys())
ls1.sort()
print(ls1)
ls2=list(d.values())
ls3=list(map(int,ls2))
ls3.sort()
print(ls3)
if 'India' in ls1:
    print('yes')
else:
    print('no')
print(sum(ls3))
