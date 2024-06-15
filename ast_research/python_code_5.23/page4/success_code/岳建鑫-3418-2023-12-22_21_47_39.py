def maxsum(nums):
    nums.sort()  # 对列表进行排序
    sum_min = 0  # 最小值的和

    for i in range(0, len(nums), 2):
        sum_min += nums[i]  # 每一对的最小值相加

    return sum_min




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

