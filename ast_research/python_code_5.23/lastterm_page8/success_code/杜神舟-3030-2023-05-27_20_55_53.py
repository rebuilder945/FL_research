a=input().split(',')
b=input().split(',')
ls=[]
for x in range(len(a)):
    c=[a[x]]+[int(b[x])]
    ls.append(c)
print(ls)
