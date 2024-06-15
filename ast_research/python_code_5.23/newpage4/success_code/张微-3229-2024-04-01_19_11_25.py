# # nums = eval(input())
# # a=[]
# # c=[]
# # f=[]
# # count=0
# # record=[0,0,0,0,0,0,0,0,0,0]
# # numrange=[0,1,2,3,4,5,6,7,8]
# # for numa in nums:
# #     for numb in numrange:
# #         if int(numa)-1 == int(numb):
# #             record[numb]=record[numb]+1
# # for i in range(9):
# #     if record[i]==1:
# #         a.append(i+1)
# #         count=count+1
# # c=sorted(a)
# # d=''.join(str(c))
# # if count==0:
# #     print("False")
# # else:
# #     # for e in d:
# #     #     if e.isdigit():
# #     #         f.append(e)
# #     # print(f)
# #     print(d)
# def find_unique_elements(nums):
#     count_dict = {}
#     unique_elements = []
#
#     # 统计每个数字出现的次数
#     for num in nums:
#         if num in count_dict:
#             count_dict[num] += 1
#         else:
#             count_dict[num] = 1
#
#     # 找出只出现一次的数字
#     for key, value in count_dict.items():
#         if value == 1:
#             unique_elements.append(key)
#
#     # 如果没有只出现一次的数字，返回False
#     if not unique_elements:
#         return False
#
#     # 升序排序并输出
#     unique_elements.sort()
#     return unique_elements
#
#
# # 用户输入部分
# input_str = input(" ")
# input_nums = [int(num) for num in input_str.split(',')]
#
# # 调用函数并输出结果
# result = find_unique_elements(input_nums)
# if result:
#     print(*result)
# else:
#     print(False)
def find_unique_elements(nums):
    unique_elements = []

    for num in nums:
        # 如果数字在列表中只出现一次，并且不在unique_elements中，则加入unique_elements
        if nums.count(num) == 1 and num not in unique_elements:
            unique_elements.append(num)
        # 如果数字在列表中出现超过一次，并且在unique_elements中，则移除unique_elements中的该数字
        elif nums.count(num) > 1 and num in unique_elements:
            unique_elements.remove(num)

    # 如果unique_elements为空，则返回False，否则返回排序后的unique_elements
    if not unique_elements:
        return False
    else:
        unique_elements.sort()
        return unique_elements


# 用户输入部分
input_str = input("请输入一个自然数列表，用逗号分隔: ")
input_nums = [int(num) for num in input_str.split(',')]

# 调用函数并输出结果
result = find_unique_elements(input_nums)
if result:
    print(*result)
else:
    print(False)
