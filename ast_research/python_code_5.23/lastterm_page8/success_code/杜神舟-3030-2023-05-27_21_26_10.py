a=input().split(',')
b=input().split(',')
ls=[]
ls2=[]
for x in range(len(a)):
    c=[a[x]]+[int(b[x])]
    ls.append(c)
    ls2.append(int(b[x]))
ls2.sort()
ls3=[]
for x in ls2:
    for y in ls:
        if y[1]==x:
            ls3.append(y)
print(ls3)
