st=input().split()
st1=list(map(eval,st))
a=(st1[1]+st1[2]+st1[3])/3
stu=dict(english=eval(st[1]),python=eval(st[2]),math=eval(st[3]))
ls=[]
for k,v in stu.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
print("%s %.2f %.2f %.2f %.2f"%(st[0],ls[0][1],ls[1][1],ls[2][1],a))

