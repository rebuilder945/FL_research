s=input().split(' ') or 'ok'
dic={}
while(s!='ok'):
    dic[s[0]]=dic.get(s[0],s[1])
    s=input()or'ok'
k=[]
v=[]
for i in dic:
    k.append(i)
for i in dic.values():
    i=int(i)
    v.append(i)
print(k)
print(v)
if 'india' in dic:
    print('yes')
else:
    print('no')
print(sum(v))
