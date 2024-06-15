def search(nums):
    n = len(nums)
    if n == 0:
        return False
    
    # 初始化候选元素和计数器
    candidate = nums[0]
    count = 1
    
    # 遍历列表，更新候选元素和计数器
    for i in range(1, n):
        if count == 0:
            candidate = nums[i]
            count = 1
        elif nums[i] == candidate:
            count += 1
        else:
            count -= 1
    






nums = eval(input())
y = search(nums)
print(y)


