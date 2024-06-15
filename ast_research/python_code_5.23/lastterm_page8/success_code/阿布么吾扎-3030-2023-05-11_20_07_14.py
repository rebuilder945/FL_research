ls1=input().split(",")
ls2=input().split(",")
d=[]
for i in range(len(ls1)):
    c=[]
    d.append(ls1[i])
    d.append(int(ls2[i]))
    c.append(d)
c.sort(key=lambda x:x[1],reverse=False)
print(c)


