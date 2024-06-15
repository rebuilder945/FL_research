list1=eval(input())
list2=[]
for i in list1:
    n=list1.count(i)
    if n==1:
        list2.append(i)
if list2==[]:
    print("False")
else:
    list2.sort()
    for x in range(len(list2)-1):
        print(list2[x],end=",")
    print(list2[len(list2)-1])
