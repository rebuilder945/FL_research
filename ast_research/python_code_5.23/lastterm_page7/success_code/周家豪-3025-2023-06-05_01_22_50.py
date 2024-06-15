lst=input().split(' ')
dic={}
for x in lst:
    dic[x]=dic.get(x,0)+1
lst2=list(dic.items())
lst2.sort()
lst2.sort(key=lambda x:x[1],reverse=True)
for x in lst2:
    if x[1]==lst2[0][1]:
        print(x[0],x[1])
    else:
        break
