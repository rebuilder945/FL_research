d={}
while True:
    s=input().split()
    if s==['ok']:
        break
    d[s[0]]=int(s[1])
m=list(d.keys())
n=list(d.values())
m.sort()
n.sort()
print(m)
print(n)
if 'India' in d:
    print('yes')
else:
    print('no')
print(sum(n))

