d={}
while True:
    s=input().split()
    if s==['ok']:
        break
    d[s[0]]=int(s[1])
print(list(d.keys()))
print(list(d.values()))
if 'India' in d:
    print('yes')
else:
    print('no')
print(sum(list(d.values())))
