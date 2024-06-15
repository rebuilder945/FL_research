g={}
i=input()
while i!='q':
    if i in g:
        g[i]+=1
    else:
        g[i]=1
    i=input()
a=0
for i in g.values():
    if i>a:
        a=i
for i in g.keys():
    if g[i]==a:
        print("{} {}".format(i,a))
