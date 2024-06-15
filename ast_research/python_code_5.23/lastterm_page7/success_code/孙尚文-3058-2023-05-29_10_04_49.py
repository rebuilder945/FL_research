a=input() or "q"
b={}
while a!="q":
    zifuchuan=a.split()
    b[a]=b.get(a,0)+1
lst=[]
for k,v in b.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
b=lst[1]
for i in b:
    print(i,end=" ")

    

