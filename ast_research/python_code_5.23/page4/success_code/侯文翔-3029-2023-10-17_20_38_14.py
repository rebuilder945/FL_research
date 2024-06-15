name=list(str(input()).split(","))
gride=eval(input())
ls=[]
for i in range(len(name)):
    a=[name[i],gride[i]]
    ls.append(a)
print(ls)
