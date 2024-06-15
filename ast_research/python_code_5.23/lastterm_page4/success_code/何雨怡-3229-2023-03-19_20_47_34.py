list=eval(input())
list2=[]
for i in range(len(list)):
    if list.count(list[i])==1:
        list2.append(list[i])
    else:
        continue
if list2==[]:
    print("False")
else:
    newlist=sorted(list2)
    final=','.join(str(i) for i in newlist)
    print(final)
    
