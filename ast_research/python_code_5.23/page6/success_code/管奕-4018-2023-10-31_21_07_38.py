def shift(lst):
    lst=list(lst)
    del lst[0]
    b=lst[0]
    lst.append(b)
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

