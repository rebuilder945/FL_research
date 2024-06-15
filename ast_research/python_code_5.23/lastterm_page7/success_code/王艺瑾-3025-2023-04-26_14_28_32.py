dic={}
a=input().split()
for y in a:
    if y in dic:
        dic[y]+=1
    else:
        dic[y]=1
list1=sorted(dic.items(),key=lambda x: x[1], reverse=True)
d=list1[0][1]
list2=[]
for i in range(len(list1)):
    if list1[i][1]==d:
        list2.append(list1[i])
for x in range(len(list2)):
    print("{} {}".format(list2[x][0],list2[x][1]))

    

            


