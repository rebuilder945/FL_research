lis=eval(input())
s=[]
jishu=0
for i in range(len(lis)-1):
    for x in range(len(lis[i])-1):
        if lis[i][x] not in s:
            s.append(lis[i][x])
            jishu=1
        else:
            jishu+=1
        a=lis[i][x]
        print("%s"%a+","+"%s"%jishu)

