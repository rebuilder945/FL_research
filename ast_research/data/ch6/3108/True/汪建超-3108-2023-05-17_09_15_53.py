lst=eval(input())
count = {}
for str in lst:
    for chr in str:
        if chr not in count:
            count[chr] = 1
        else:
            count[chr] += 1
for x in sorted(count.keys()):
    print("%c,%d"%(x,count[x]))

# str_list_str = input("请输入仅包括字符串对象的列表：")
# # 将输入的字符串转换为列表对象
# str_list = ast.literal_eval(str_list_str)

# # 初始化字典
# count_dict = {}
# for c in "abcdefghijklmnopqrstuvwxyz":
#     count_dict[c] = 0 # 所有字母的初始出现次数都为0

# # 遍历字符串列表
# for s in str_list:
#     # 遍历字符串中的每个字符
#     for c in s:
#         count_dict[c] += 1 # 更新对应字母的出现次数

# # 按照a到z的顺序输出每个字母和其出现的次数
# for c in "abcdefghijklmnopqrstuvwxyz":
#     if count_dict[c] != 0:
#         print("{},{}".format(c, count_dict[c]))

