a=input().split()
dic={}
lst=[]
for i in a:
    dic[i]=dic.get(i,0)+1
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
lst2=[]
maxsum=lst[0][1]
for i in lst:
    if i[1]==maxsum:
        lst2.append(i[0])
for i in lst2:
    print("{} {}".format(i,maxsum))


