list1=[x for x in range(1,eval(input())+1)]
list2=list1.copy()
for i in range(len(list2)-1):
    list2[i]=list2[i+1]
y=list2.pop()
list3=list2+[list1[0]]
print(list3)
