name=input().split(',')
grade=input().split(',')
dic={}
for i in range(len(name)):
    dic[name[i]]=eval(grade[i])

jack=list(dic.items())
jack.sort(key=lambda x:x[1],reverse=False)
jack=[]
lst=list(dic.keys())
lst1=list(dic.values())
for i in range(len(name)):
    a,b=lst[i],lst1[i]
    jack.append([a,b])
print(jack)
