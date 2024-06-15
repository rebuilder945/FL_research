def shift(lst):
    a=lst[-1]
    ls=lst[:-1]
    a=list(a)
    ls.extend(a)
    return ls

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

