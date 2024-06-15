i=input()
g={}
while i!='q':
    if i in g:
        g[i]+=1
    else:
        g[i]=1
    i=input()
jishu=0
for i in g.values():
    if i>jishu:
        jishu=i
    else:
        pass
for i in g.keys():
    if i==jishu:
        print('%s %s'%(i,jishu))
