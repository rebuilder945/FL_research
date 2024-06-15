def jm(x):
    return (int(x)+5)%10
list1=input()
list2=[]
for i in range(len(list1)):
    list2.append(list1[i])
list2=list(map(jm,list2))
list2[0],list2[-1]=list2[-1],list2[0]
list2[1],list2[-2]=list2[-2],list2[1]
for m in range(len(list2)):
    print(list2[m],end="")


