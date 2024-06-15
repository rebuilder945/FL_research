def shift(lst):
    listlst=list(lst)
    listlst2=listlst.copy()
    lastone=listlst2[-1]
    listlst.remove(lastone)
    listlst.insert(0,lastone)
    lst=listlst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

