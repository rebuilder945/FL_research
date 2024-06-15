st=input().split()
a=(eval(st[1])+eval(st[2])+eval(st[3]))/3
stu=dict(english=eval(st[1]),python=eval(st[2]),math=eval(st[3]))
ls=[]
for k,v in stu.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
print("%s %.2f %.2f %.2f %.2f"%(st[0],ls[0][1],ls[1][1],ls[2][1],a))

