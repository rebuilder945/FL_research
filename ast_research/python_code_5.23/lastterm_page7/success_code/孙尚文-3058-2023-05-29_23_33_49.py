
b={}
while input()!="q":
    zifuchuan=input().split()
    c=zifuchuan[0]
    b[c]=b.get(c,0)+1
lst=[]
for k,v in b.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
b=lst[1]
for i in b:
    print(i,end=" ")

    

