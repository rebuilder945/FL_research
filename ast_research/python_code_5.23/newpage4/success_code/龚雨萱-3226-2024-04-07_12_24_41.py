def search(nums):
    for i in nums:
        if nums.count(i)>lun(nums)//2:
            return i
    return false





nums = eval(input())
y = search(nums)
print(y)


