lst=eval(input())
s=""
zm=[]
zmc=[]
for i in lst:
    s+=str(i)
s="".join(sorted(s))
for j in s:
    if j not in zm:
        zm.append(j)
        zmc.append([j,s.count(j)])
for k in range(0,len(zmc)):
    print("%s,%d"%(zmc[k][0],zmc[k][1]))
