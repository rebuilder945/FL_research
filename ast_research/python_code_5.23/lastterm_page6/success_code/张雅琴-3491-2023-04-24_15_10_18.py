def shift(lst):
    b = lst.pop()
    import copy
    lst = copy.deepcopy([b] + lst)


list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

