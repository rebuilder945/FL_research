g={}
i=input()
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
for i in g.keys():
    if g[i]==jishu:
        print("{} {}".format(i,jishu))
