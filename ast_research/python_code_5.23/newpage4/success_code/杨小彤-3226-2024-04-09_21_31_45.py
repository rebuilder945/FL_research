def search(nums):
    n == len(nums)
    for x in nums:
        if nums.count(x)>=(n//2):
            return nums[x]
        else:
            print("False")






nums = eval(input())
y = search(nums)
print(y)


