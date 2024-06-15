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
    print(int(list2))

