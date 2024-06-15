a=input().split()
dic={}
for i in a:
    dic[i]=dic.get(i,0)+1
lst=list(dic.items())
lst.sort(key=lambda x:x[1],reverse=True)
for i in range(1,len(lst)):
    if lst[i][1]==lst[0][1]:
        print(lst[0][0],lst[0][1])
        print(lst[i][0],lst[i][1])
        break
