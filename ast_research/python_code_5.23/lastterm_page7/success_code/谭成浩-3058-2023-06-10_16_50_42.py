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
for i in x.keys():
    if x[i]==jishu:
        print('{} {}'.format(i,jishu))
