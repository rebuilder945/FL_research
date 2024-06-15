def shift(lst):
    s=lst[-1]
    lst=[s]+lst[0:-1]
    return lst

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

