list1=eval(input())
list2=[]
for x1 in list1:
    times=list1.count(x1)
    if times==1:
       list2.append(x1)
       list2.sort()
       print(list2)
    if times>1:
       print("False")
