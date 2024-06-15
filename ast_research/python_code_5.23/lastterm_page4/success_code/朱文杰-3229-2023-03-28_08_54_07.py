n=eval(input())
m=[]
for x in n:
    if n.count(x)==1:
        m.append(x)
m.sort()
if len(m)==0:
    print(False)
else:
    str1=",".join(map(str,m))
print(str1)
