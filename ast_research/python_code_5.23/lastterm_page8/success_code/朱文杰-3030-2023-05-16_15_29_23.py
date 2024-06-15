name=input().split(",")
grade=input().split(",")
lst=[]
for x in range(len(name)):
    lst.append([name[x],int(grade[x])])
lst.sort(key=lambda x:x[1],reverse=False)
print(lst)
