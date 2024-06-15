def max_number(nums):
    # 将数字转换为字符串
    nums = [str(num) for num in nums]
    # 对字符串进行排序，按照降序排列
    nums.sort(reverse=True)
    # 将排序后的字符串连接起来，得到最大的整数
    max_num = int(''.join(nums))
    return max_num

nums_str = input()
nums = [int(num) for num in nums_str.split(",")]
result = max_number(nums)
print(result)


