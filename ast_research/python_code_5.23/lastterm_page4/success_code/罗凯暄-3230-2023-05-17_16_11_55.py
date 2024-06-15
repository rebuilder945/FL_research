nums = input().split()  # 读入数字列表
nums.sort(reverse=True)  # 按照从大到小排序
result = ""
for num in nums:
    if num not in result:  # 如果该数字还没有被使用过
        result += num
print(result)

