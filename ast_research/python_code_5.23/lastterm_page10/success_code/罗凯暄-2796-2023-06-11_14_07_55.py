import re

s = input()  # 读入字符串
nums = re.findall(r'\d+', s)  # 匹配数字子串
if not nums:  # 如果没有数字子串
    print("No digits")
else:
    max_num = max(nums, key=len)  # 找出最长的数字子串
    print(max_num)

