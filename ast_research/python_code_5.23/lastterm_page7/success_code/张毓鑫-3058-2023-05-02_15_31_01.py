a=input()
b=[]
c={}
while a!='q':
    if a not in b:
        b.append(a)
        c[a]=1
    elif a in b:
        c[a]+=1
    a=input()
e=max(c.values())
for i in c.keys():
    if c[i]==e:
        print(i,e)

