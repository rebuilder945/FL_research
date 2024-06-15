lst = eval(input())
b=''
for i in lst:
    for j in i:
        b+=j
a=[]
for i in b:
    s=b.count(i)
    if s>0:
        pass
    else:
        x=(i,s)
        a.append(x)
a.sort(key=lambda x:x[0])
for i in a:
    print(i[0],i[1])
