a=eval(input())
list1=[]
list2=[]
def Fi(a):
    first=1
    last=1
    for i in range(a):
        now=first+last
        first=last
        last=now
        list1.append(now)
    return list1
def Fin(a):
    first1=0
    last1=1
    for x in range(a):
        now1=first1+last1
        first1=last1
        last1=now1
        list2.append(now1)
    return list2
list3=[]
Fi(a)
Fin(a)
for m in range(a):
    list3.append(list1[m]/list2[m])
result=sum(list3)
print("%.3f"%result)

