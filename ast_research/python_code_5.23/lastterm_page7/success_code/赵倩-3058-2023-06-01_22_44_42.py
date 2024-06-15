a=input() or"q"

d={}
while a!="q":
    if a in d:
        
        d[a]+=1
    else:
        d[a]=1
    a=input() or"q"
l=[]
for i in d:
    b=d[i]
    l.append(b)
n=max(l)
for key in d:
    if d[key]==n:
        print(key,n)

                    




