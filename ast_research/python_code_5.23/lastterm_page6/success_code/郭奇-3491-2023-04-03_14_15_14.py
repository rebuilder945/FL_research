def shift(lst):
    list = lst.remove([-1])
    list1 = lst[-1] + list
    return list1

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

