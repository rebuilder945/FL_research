ls1=input().split(',')
ls2=list(map(int,input().split(',')))
a=list(zip(ls1,ls2))
a.sort(key=lambda x:x[-1])
ls=[]
for x in a:
    x=list(x)
    ls.append(x)
print(ls)


