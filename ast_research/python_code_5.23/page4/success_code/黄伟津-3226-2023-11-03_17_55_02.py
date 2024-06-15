def search(nums):
    lstCount = [nums.count(x) for x in nums]
    maxN = max(lstCount)
    imax = lstCount.index(maxN)
    if maxN > len(nums) // 2:
        return nums[imax]
    else:
        return False






nums = eval(input())
y = search(nums)
print(y)


