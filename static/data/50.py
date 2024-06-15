def calDegrees(nums):
    import random
    n = random.sample(nums, 1)  # 将 random.sample(nums) 修改为 random.sample(nums, 1)，指定抽取一个样本
    count = nums.count(n[0])  # 通过 n[0] 获取抽样结果，并统计其在 nums 中出现的次数
    return count

nums = eval(input())
d = calDegrees(nums)
print(d)