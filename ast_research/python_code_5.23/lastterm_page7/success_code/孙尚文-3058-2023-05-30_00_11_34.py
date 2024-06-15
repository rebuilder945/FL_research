b={}

a=input() or "q"
while a!="q":
    
    b[a]=b.get(a,0)+1
lst=[]
for k,v in b.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
c=lst[0][0]
d=lst[0][1]
print("{} {}".format(c,d))
