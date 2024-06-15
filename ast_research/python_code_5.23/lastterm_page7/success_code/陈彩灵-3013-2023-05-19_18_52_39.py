counlist=[]
ss=input()
while ss!='ok':
    s=ss.split(' ')
    counlist.append((s[0],int(s[1])))
    ss=input()
dic=dict(counlist)
ankey=list(dic.keys())
anva=list(dic.values())
ankey.sort()
print(ankey)
print(sorted(anva))
if 'India' in ankey:
    print('yes')
else:
    print('no')
print(sum(anva))
