n=input().split()
dic={}
for x in n:
    dic[x]=dic.get(x,0)+1
lst=list(dic.items())
lst.sort(key=lambda x:x[1],reverse=True)
lst2=[]
if len(lst)==1:
    print(lst[0][0],lst[0][1])
else:
    if lst[0][1]==lst[1][1]:
        for i in lst:
            if i[1]!=lst[0][1]:
                break
            else:
                lst2.append(i)
        lst2.sort(key=lambda x:x[0])
        for x in lst2:
            print(x[0],x[1])
    else:
        print(lst[0][0],lst[0][1])



