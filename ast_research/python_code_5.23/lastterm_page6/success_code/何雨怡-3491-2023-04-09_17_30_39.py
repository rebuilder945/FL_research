def shift(lst):
    listlst=list(lst)
    a=listlst[-1]
    del listlst[-1]
    listlst.insert(0,a)
    return listlst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

