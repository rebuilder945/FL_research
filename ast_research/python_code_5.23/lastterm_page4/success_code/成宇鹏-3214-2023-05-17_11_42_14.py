# 读入一个整数列表，把数值为0的元素移动到列表尾部，其他元素的相对顺序不变。输出调整后的列表。
# lst = eval(input())
# a = 0
# for x in lst:
#     if x == 0:
#         lst.remove(0)
#         a += 1
# b = [0]*a
# lst1 = lst + b
# print(lst1)
        
lst = eval(input())
a = lst.count(0)
lst1 =[]
for x in lst:
    if x != 0:
        lst1.append(x)
b = [0]*a
lst2 = lst1 + b
print(lst2)
        
