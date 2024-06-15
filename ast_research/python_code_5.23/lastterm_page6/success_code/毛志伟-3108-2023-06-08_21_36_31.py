s1 = eval(input())
s2 = {}
for x in s1:
    for i in x:
        if i not in s2:
            s2[i]=1
        else:
            s2[i]+=1
s2 = sorted(s2.items(),key = lambda x:x[0])
s2 = [list(x) for x in s2]
for x in s2:
    print("%s,%d"%(x[0],x[1]))
