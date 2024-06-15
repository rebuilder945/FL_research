a=input()
b={}
while a!='q':
    if a in b:
        b[a]+=1
    else:
        b[a]=1
    a=input()    
c=0        
for x in b.values():
    if x>c:
        c=x
for x in b.keys():
    if b[x]==c:
        print(x,c)                
