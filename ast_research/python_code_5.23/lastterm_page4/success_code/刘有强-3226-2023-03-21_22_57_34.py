def search(nums):
    sss=0
    for i in nums:
        if nums.count(i) >= len(nums)//2:
            sss=nums.count(i)
        else:
            sss="False"
    return sss





nums = eval(input())
y = search(nums)
print(y)


