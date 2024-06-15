dic={}
s=input().split()
for x in s:
    dic[x]=dic.get(x,0)+1#有x则+1，无则返回0
    lst=list(dic.items())
    maxv=max(list(dic.values()))
lst.sort(key=lambda x: x[0])
for x in lst:
    if x[1]==maxv:
        print(x[0],x[1])
