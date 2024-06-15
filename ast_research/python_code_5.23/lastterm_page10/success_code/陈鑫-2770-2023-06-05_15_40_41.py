a=input()
b=input()
c={}
d={}
for i in a:
    c[i]=c.get(i,0)+1
for i in b:
    d[i]=d.get(i,0)+1 
if c==d:
    print('True')
else:
    print('False')   


