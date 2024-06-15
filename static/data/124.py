def shift(lst):
    for i in reversed(range(len(lst))):
        #reversed() 函数期望接收一个可迭代对象，但却传递了一个整数（len(lst) 返回一个整数）
        if i > 0:
            lst[i] = lst[i-1]
        else:
            lst[i] = lst[-1]
    return lst

list1 = input().split(",")
shifted_list = shift(list1.copy())
print(shifted_list)