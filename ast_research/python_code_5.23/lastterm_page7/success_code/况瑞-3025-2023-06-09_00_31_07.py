s=input().split()
ls=sorted(list(s))
dic={}
Max=0
for i in ls:
    dic[i]=dic.get(i,0)+1

    if dic[i]>=Max:
        Max=dic[i]
for k,v in dic.items():
    if v==Max:
        print(k,v)



