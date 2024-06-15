lis=eval(input())
s={}
jishu=0
for i in range(len(lis)-1):
    for x in range(len(lis[i])-1):
        if lis[i][x] not in s:
            s[i]=1
        else:
            s[i]+=1
s= list(s.items())
s1=[]
for i in s:
    s1.append(list(i))
s1.sort()
for x in s1:
    print("%s,%d" % (x[0], x[1]))

