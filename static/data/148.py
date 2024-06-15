def find_degree(nums):#函数名中间应该是一个下划线而不是空格
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    return counts

nums = eval(input())
d = find_degree(nums)  # 调用自定义函数
print(d)