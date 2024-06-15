a=input()
b={}
while a!="q":
    b[a]=b.get(a,0)+1    
    a=input()
print(list(b.keys())[0])
c=list(map(int,b.values()))
for i in range(len(c)):
    if c[i]==max(c):
        print(c[i]) 

