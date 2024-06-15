b=input().split(" ")
c={}
for i in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
jishu=0
for i in c.values():
    if i>jishu:
        jishu=i
for i in c.keys():
    if c[i]==jishu:
        print("{} {}".format(i,jishu))


