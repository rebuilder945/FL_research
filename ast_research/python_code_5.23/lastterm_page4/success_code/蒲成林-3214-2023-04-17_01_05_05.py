def zeros(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)
    return nums

nums=eval(input())
print(zeros(nums))
