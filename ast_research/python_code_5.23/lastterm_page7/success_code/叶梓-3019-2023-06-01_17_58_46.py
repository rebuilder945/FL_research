list=input().split()
list2=list[1:]
list2 = list(map(int,list2))
avg=sum(list2)/len(list2)
list2.sorted(reversed=True)
print(list[0],"%.2f %.2f %.2f %.2f"%(list2[0],list2[1],list2[2],avg))
