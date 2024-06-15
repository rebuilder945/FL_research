def shift(lst):
    list2 = list(lst)
    if not list2:  # 如果输入的列表为空，则返回空列表
        return []
    list3 = [list2[-1]]  # 将list2的最后一个元素作为list3的第一个元素
    for i in list2[:-1]:  # 遍历list2的除最后一个元素外的其他元素
        list3.append(i)  # 将元素添加到list3中
    return list3
#在创建空列表 list3 后，直接对其索引为 0 的位置进行赋值，
#但是由于列表是空的，因此会产生 "list assignment index out of range" 错误。

list1 = input().split(",")  # 输入格式 1,2,3,4,5
result = shift(list1)
print(result)