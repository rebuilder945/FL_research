a=eval(input())
dic={}
for i in a:
    for x in "abcdefghijklmnopqrstuvwxyz":
        if i.count(x)!=0 and x not in dic:
            dic[x]=i.count(x)
        elif i.count(x)!=0 and x in dic:
            dic[x]+=i.count(x)
        else:
            continue
ls=list(dic.items())
def paixu(x):
    return x[0]
ls.sort(key=paixu)
for i in ls:
    print(i[0],end="")
    print(",",end="")
    print(i[1])

