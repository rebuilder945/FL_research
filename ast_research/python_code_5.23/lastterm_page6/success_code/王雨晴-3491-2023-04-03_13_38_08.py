def shift(lst):
    lst.insert(len(lst),lst[0])
    lst.remove(lst[0])
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

