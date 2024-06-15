def search(nums):
    for i in nums:
        if nums.count(i)>len(nums):
            return i
        else:
            return 0





nums = eval(input())
y = search(nums)
print(y)


