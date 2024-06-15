g={}
i=input()
while i!="q":
    if i in g:
        g[i]+=1
    else:
        g[i]=1
a=0
for x in g.values():
    if x>a:
        a=i
for x in g.keys():
    if g[i]==a:
        print("{}{}".format(i,a))        
