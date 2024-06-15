s = eval(input())
a = {}
for x in s:
    for i in x:
        if i not in a :
            a[i]=1
        else:
            a[i]+=1
a = sorted(a.items(),key=lambda x:x[0])
a = [list(x) for x in a]
for j in a:
    print("%s,%d"%(j[0],j[1]))
