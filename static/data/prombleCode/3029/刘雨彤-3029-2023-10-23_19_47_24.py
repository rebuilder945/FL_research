name=input().split("," )
arade=eval(input())
ls=[]
for i in range(len(name)):
    item=[]
    item.append(name[i])
    item.append(arade[i])
    ls.append(item)
print(ls)    
ls=[[name[i],grade[i]] for i in range(len(name))]

