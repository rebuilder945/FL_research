# 从标准输入中读取正整数列表
nums = list(map(int, input().split()))

# 将列表中的数字按照字符串比较大小的方式排序
nums_str = list(map(str, nums))
nums_str.sort(reverse=True)

# 拼接排序后的字符串，形成最大整数
max_num_str = ''.join(nums_str)

# 输出最大整数
print(int(max_num_str))

