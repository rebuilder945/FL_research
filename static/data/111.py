def shift(lst):
    lst = list(lst)
    a = lst[-1]
    for i in range(len(lst)-1, 0, -1):
        #len 是一个内置函数，你需要调用它来获取列表的长度，所以应该写成 len(lst) 而不是 len-1。
        lst[i] = lst[i-1]
    lst[0] = a
    return lst

list1 = input("请输入一个以逗号分隔的数字序列：").split(",")
list1 = shift(list1)
print(list1)