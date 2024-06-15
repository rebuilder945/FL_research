shu  =  input().split(" ")
dian={}
li1=[]
for x in shu:
    dian[x]=dian.get(x,0)+1
lis=list(dian.items())
lis.sort(key=lambda x: x[1],reverse=True)
for x in lis:
    if x[1]==lis[0][1]:
        li1.append(x)
li1.sort()
for x in li1:
    print(x[0],x[1])
