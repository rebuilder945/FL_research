lst=input().split()
dic={}
for i in lst:
    dic[i]=dic.get(i,0)+1
newlst=list(dic.items())
newlst.sort(key=lambda x:x[1],reverse=True)
for i in range(2):
    print(newlst[i][0],newlst[i][1])
