lst = eval(input())  # 将字符串输入转换为列表

zeros = lst.count(0)  # 统计列表中0的个数
lst = [x for x in lst if x != 0]  # 将非零元素提取出来

lst += [0] * zeros  # 在列表尾部添加相应个数的0
print(lst)

