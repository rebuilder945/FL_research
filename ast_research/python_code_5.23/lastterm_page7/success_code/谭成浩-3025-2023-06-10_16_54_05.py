n=input()
x={}
while n!='q':
    if n not in x:
         x[n]=1
    else:
        x[n]+=1
    n=input()
jishu=0
for i in x.values():
    if i>jishu:
        jishu=i
c=[]
for i in x.keys():
    if x[i]==jishu:
        c.append(i)
c.sort()
for i in c:
    print('{} {}'.format(i,jishu))
