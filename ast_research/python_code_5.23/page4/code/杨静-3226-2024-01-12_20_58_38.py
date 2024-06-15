def search(nums):
    n=len(nums)//2
    nums.sort（）
    major=nums[n//2]
    if nums.count(major)>n:
        return major
    else:
        return 'False'





nums = eval(input())
y = search(nums)
print(y)


