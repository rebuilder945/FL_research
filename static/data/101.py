def shift(lst):
    lst.insert(0, lst.pop())  # 使用 lst.pop() 删除并返回列表末尾的元素
    return lst

list1 = input("请输入一个用逗号分隔的列表：").split(",")  # 输入格式 1,2,3,4,5
shift(list1)
print(list1)