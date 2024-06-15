def shift(lst):
    lst = list(list1)
    a = lst[-1]
    del lst[-1]
    lst1 = lst.insert(0,a)
    return lst1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

