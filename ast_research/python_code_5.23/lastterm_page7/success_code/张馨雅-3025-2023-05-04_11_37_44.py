s=input().split
dic={}
for i in s():
    dic[i]=dic.get(i,0)+1
lst=[]
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
print('{} {}'.format((lst[0][0]),(lst[0][1])))
if lst[1][1]==lst[0][1]:
    print('{} {}'.format((lst[1][0]),(lst[1][1])))



