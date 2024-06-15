#12在列表中找出只出现一次的元素，并排序输出
from collections import Counter

# 读入输入并转换为列表
num_list = eval(input())

# 统计每个数字出现的次数
counter = Counter(num_list)

# 遍历列表，找出只出现一次的数字
unique_nums = []
for num in num_list:
    if counter[num] == 1:
        unique_nums.append(num)

# 如果没有只出现一次的数字，则输出False
if len(unique_nums) == 0:
    print(False)
else:
    # 对只出现一次的数字进行排序并输出
    unique_nums.sort()
    print(",".join(str(num) for num in unique_nums))

