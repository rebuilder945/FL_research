a=input()
b={}
while a!="q":
    b[a]=b.get(a,0)+1    
    a=input()
print(b)
c=list(map(int,b.values()))
print(c)
