# num_str = input()
# num_list = list(num_str)
# for i in range(len(num_list)):
#     num_list[i] = str((int(num_list[i]) + 5) % 10)
# num_list.reverse()
# encrypted_num = ''.join(num_list)
# print(encrypted_num)


# stu_list = [
#     ['201801', 'zhangyi'], ['201802', 'zhanger'], ['201803', 'zhangsan'], ['201804', 'zhangsi'],
#     ['201805', 'wangyi'], ['201806', 'wanger'], ['201807', 'wangsan'], ['201808', 'wangsi'],
#     ['201809', 'liyi'], ['201810', 'lier'], ['201811', 'lisan'], ['201812', 'lisi'],
#     ['201813', 'zhaoyi'], ['201814', 'zhaoer'], ['201815', 'zhaosan'], ['201816', 'zhaosi'],
#     ['201817', 'zhouyi'], ['201818', 'zhouer'], ['201819', 'zhousan'], ['201820', 'zhousi']
# ]

# def binary_search(stu_list, target):
#     left, right = 0, len(stu_list) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if stu_list[mid][0] == target:
#             return stu_list[mid]
#         elif stu_list[mid][0] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return None

# # 从键盘读取输入的学号
# target = input()

# # 使用二分查找查找学号对应的学生
# result = binary_search(stu_list, target)

# # 输出查找结果
# if result:
#     print(result[0] + result[1])
# else:
#     print(None)


n = int(input())

numerator = 2
denominator = 1
total_sum = 2 / 1  # 第一项是2/1

for i in range(1, n):
    next_numerator = numerator + denominator
    next_denominator = numerator
    total_sum += next_numerator / next_denominator
    numerator, denominator = next_numerator, next_denominator

print('{:.4f}'.format(total_sum))

