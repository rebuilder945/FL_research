a=eval(input())
b=a.split('')
c={}
for i in b:
    if i not in c.keys():
        c[i]=1
    elif i in c.keys():
        c[i]+=1
e=max(c.values())
for i in c.keys():
    if c[i]==e:
        print(i,e)
