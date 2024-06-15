n=eval(input())
a=[]
for i in n:
    if n.count(i)==1:
        a.append(i)
        a.sort()
    else:
        continue
if len(a)==0:
    a="False"
print(a)
