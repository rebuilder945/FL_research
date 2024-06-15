s=input().split
dic={}
for i in s():
    dic[i]=dic.get(i,0)+1
lst=[]
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
print('{} {}'.format((lst[0][0]),(lst[0][1])))
for i in range(1,len(lst)):
    if lst[i][1]==lst[0][1]:
        print('{} {}'.format((lst[i][0]),(lst[i][1])))



