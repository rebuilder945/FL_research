def shift(lst):
n = len(lst)
    # 将最后一个元素移动到最前面
    list1.insert(0, list1.pop(n-1))
    return list1

# 读入列表并输出循环右移一位后的列表
list1 = input().split(',')
list1 = [int(x) for x in list1]  

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

