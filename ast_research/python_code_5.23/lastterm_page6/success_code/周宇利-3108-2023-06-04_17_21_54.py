list1=eval(input())
for i in list1:
    list2=list(i)
    for j in list2:
        list2.sort()
        a=b=list2.count(j)
        while b>1:
            list2.remove(j)
            b-=1
        print(j,end=",")
        print(a)
