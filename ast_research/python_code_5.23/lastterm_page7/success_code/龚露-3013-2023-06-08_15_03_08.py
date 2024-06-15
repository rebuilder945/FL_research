d={}
while True:
    s=input().split()
    if s==['ok']:
        break
    d[s[0]]=int(s[1])
m=list(d.keys())
n=list(d.values())
print(m.sort())
print(n.sort())
if 'India' in d:
    print('yes')
else:
    print('no')
print(sum(list(d.values())))
