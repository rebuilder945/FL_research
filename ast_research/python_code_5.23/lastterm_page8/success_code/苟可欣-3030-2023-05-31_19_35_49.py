a="1123"
b="405"
al=[]
bl=[]
k=0
for x in a:
    al.append(x)
for x in b :
    bl.append(x)
for i in range(1,len(bl)+1):
    k=k+(int(al[-i])*int(bl[-i]))
    if i==len(bl) or i==len(al):
        break
print (k)
