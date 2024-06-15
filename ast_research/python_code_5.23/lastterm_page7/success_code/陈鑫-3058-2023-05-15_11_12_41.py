a=input()
b={}
while a!="q":
    b[a]=b.get(a,0)+1    
    a=input()
c=list(map(int,b.values()))
for i in range(len(c)):
    if c[i]==max(c):
        print(list(b.keys())[i],c[i]) 

