def shift(lst):
n = len(lst)
    # 将最后一个元素移动到最前面
    lst.insert(0, lst.pop(n-1))
    return lst

# 读入列表并输出循环右移一位后的列表
lst = input().split(',')
lst1 = [int(x) for x in lst]  

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

