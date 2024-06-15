def search(nums:list):
    for i in range(len(nums)):
        if nums.count(nums[i-1]) > len(nums)//2:
            return nums[i-1]
        else:
            return "False"





nums = eval(input())
y = search(nums)
print(y)


