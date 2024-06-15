lst=list(input().split(" "))
dic={}
lst0=[]
for x in lst:
    dic[x]=dic.get(x,0)+1
for x,y in dic.items():
    lst0.append([x,y])
lst0.sort(key=lambda x:x[1],reverse=True)
for x in range(0,len(lst0)):
    if lst0[x][1]==lst0[0][1]:
        print(str(lst0[x][0])+" "+str(lst0[x][1]))

