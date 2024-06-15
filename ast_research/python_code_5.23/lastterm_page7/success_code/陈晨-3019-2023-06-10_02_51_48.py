lst1 = input().split()
dic={}
dic["eng"]=lst1[1]
dic["pyt"]=lst1[2]
dic["mat"]=lst1[3]
lst=[]
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
avg=(int(lst1[1])+int(lst1[2])+int(lst1[3]))/3
print(lst1[0],"%.2f %.2f %.2f %.2f"%(lst[0][1],lst[1][1],lst[2][1],avg))
