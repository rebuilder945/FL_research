lst=input().split()
dic={}
for i in lst:
    dic[i]=dic.get(i,0)+1
newlst=list(dic.items())
newlst.sort(key=lambda x:x[1],reverse=True)
final=[]
for i in range(len(newlst)):
    if newlst[i][1]==newlst[0][1]:
        final.append(newlst[i])
final.sort(key=lambda x:x[0])
for i in final:
    print(i[0],i[1])
