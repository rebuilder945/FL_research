g={}
i=input()
while i!="q":
    if i in g:
        g[i]+=1
    else:
        g[i]=1
    i=input()    
a=0
for x in g.values():
    if x>a:
        a=x
for x in g.keys():
    if g[x]==a:
        print("{}{}".format(x,a))        
