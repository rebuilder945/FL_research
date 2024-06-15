a=input()
b={}
while a!='ok':
    m,n=map(str,a.split())
    b[m]=int(n)
    a=input()
c=[]
d=[]    
for x in b.keys():
    c.append(x)
for x in b.values():
    d.append(x)
c.sort()
d.sort()    
print(c)
print(d)    
if 'india'in b:
    print("yes")
else:
    print("no") 
s=0         
for x in b.values(): 
    s=s+x
print(s)         
        
