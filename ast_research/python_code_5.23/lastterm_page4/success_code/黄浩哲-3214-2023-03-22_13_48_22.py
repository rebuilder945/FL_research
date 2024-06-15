def moveZeroes(nums):
    for i in range(len(nums)):
        flag = True
        for j in range(len(nums) - i - 1):
            if nums[j] == 0 and nums[j + 1] != 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = False
        if flag:
            break
    return nums
