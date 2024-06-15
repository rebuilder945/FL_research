list1=list(input().split())
d={}
for i in list1:
    if i=="q":
        list1.remove(i)
    else:
        d[i]=list1.count(i)
    print("{}{}".format(i,list1.count(i)))

