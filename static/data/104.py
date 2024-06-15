
def shift(lst):
    a = lst.pop(-1)
    lst.insert(0, a)
    return lst

list1 = [int(x) for x in input("请输入一个用逗号分隔的整数列表：").split(",")]  
# 将输入的字符串转换为整数列表
shifted_list = shift(list1)

print(shifted_list)