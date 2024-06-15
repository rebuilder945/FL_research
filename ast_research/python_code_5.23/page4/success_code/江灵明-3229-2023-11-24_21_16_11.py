a = eval(input());b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
    c=b.copy()
if c==[]:
    print('False')
else:
    c.sort()
    print(*c,sep=",")
