list1=eval(input())
list2=[]
for x in list1:
    b=list1.count(x)
    if b==1:
        list2.append(x)
list2.sort(reverse=False)
if list2==[]:
    print("False")
if list2!=[]:
    print(*list2,sep=",")

