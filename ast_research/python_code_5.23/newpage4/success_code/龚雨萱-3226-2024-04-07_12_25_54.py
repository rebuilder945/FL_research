def search(nums):
    for n in nums:
        if nums.count(n)>lun(nums)//2:
            return n
    return False





nums = eval(input())
y = search(nums)
print(y)


