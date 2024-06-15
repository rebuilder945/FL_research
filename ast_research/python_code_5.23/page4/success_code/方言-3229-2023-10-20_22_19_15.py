list=eval(input())
dic={}
sc=[]
for i in list:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in dic.keys():
    if dic[j]==1:
        sc.append(dic(j))
if sc==[]:
    print('False')
else:
    print(sc)
