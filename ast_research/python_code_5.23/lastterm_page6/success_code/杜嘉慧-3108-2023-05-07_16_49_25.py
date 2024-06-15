s=eval(input())
num={}
for x in s:
    for i in x:
        if i not in num:
            num[i]=1
        else:
            num[i]+=1
num=sorted(num.items(),key=lambda x:x[0])
num=[list(x) for x in num]
for x in s:
    print("%num,%d"%(x[0],x[1]))
