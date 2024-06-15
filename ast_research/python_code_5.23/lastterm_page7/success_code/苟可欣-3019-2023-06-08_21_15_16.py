n=input().split()
ls=[]
for x in n[1:]:
    ls.append(int(x))
avg=sum(ls)/3
ls.sort(reverse=True)
print("%s %.2f %.2f %.2f %.2f"%(n[0],ls[0],ls[1],ls[2],avg))
