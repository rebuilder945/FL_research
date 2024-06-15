lst1=input().split()
dic1={}
for i in lst1:
    dic1[i]=dic1.get(i,0)+1

lst2=[]
for k,v in dic1.items():
    lst2.append([k,v])

lst2.sort(key=lambda x:x[1],reverse=True)
for i in range(len(lst2)):
    if lst2[i][1]==lst2[0][1]:
        print(lst2[i][0],lst2[i][1])
