s=input() or 'ok'
dic={}
while(s!='ok'):
    a,b=map(str,s.split(' '))
    dic[a]=int(b)
    s=input()or'ok'
k=[]
v=[]
for i in dic:
    k.append(i)
for i in dic.values():
    v.append(i)
k.sort(reverse=True)
v.sort(reverse=True)
print(k)
print(v)
if 'india' in k:
    print('yes')
else:
    print('no')
print(sum(v))
